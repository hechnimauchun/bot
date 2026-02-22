import geopy
from telegram import KeyboardButton, ReplyKeyboardMarkup
from db import *
from geopy.geocoders import Nominatim
from translations import t

agent = geopy.geocoders.Nominatim(user_agent="royxatdan_ot")

def royxatdan_ot(update, context):
    tugmalar = ReplyKeyboardMarkup([
        [KeyboardButton(t(context, "ism_tugma")), KeyboardButton(t(context, "familiya_tugma"))],
        [KeyboardButton(t(context, "tel_tugma"), request_contact=True)],
        [KeyboardButton(t(context, "lokatsiya_tugma"), request_location=True)],
    ], resize_keyboard=True)
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text=t(context, "royxatdan_oting"), reply_markup=tugmalar)

def ism(update, context):
    context.user_data['holat'] = 'ism'
    update.message.reply_text(t(context, "ism_yuborish"))

def familiya(update, context):
    context.user_data['holat'] = 'familiya'
    update.message.reply_text(t(context, "familiya_yuborish"))

def matn_qabul(update, context):
    text = update.message.text
    holat = context.user_data.get('holat')

    if holat == 'ism':
        context.user_data['ism'] = text
        context.user_data['holat'] = None
        update.message.reply_text(t(context, "ism_qabul"))

    elif holat == 'familiya':
        context.user_data['familiya'] = text
        context.user_data['holat'] = None
        update.message.reply_text(t(context, "familiya_qabul"))

def tel_nomer(update, context):
    nomer = update.message.contact.phone_number
    context.user_data['tel_nomer'] = nomer
    update.message.reply_text(t(context, "tel_qabul"))

def lokatsiya(update, context):
    lat = update.message.location.latitude
    lon = update.message.location.longitude
    manzil = agent.reverse(f"{lat}, {lon}", language="uz")
    manzil_nomi = manzil.address if manzil else f"{lat}, {lon}"
    context.user_data['lokatsiya'] = manzil_nomi

    user_id = update.effective_user.id
    ism = context.user_data.get('ism', '')
    familiya = context.user_data.get('familiya', '')
    tel_nomer = context.user_data.get('tel_nomer', '')

    cursor.execute("""
        INSERT OR REPLACE INTO users (user_id, ism, familiya, tel_nomer, lokatsiya)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, ism, familiya, tel_nomer, manzil_nomi))
    conn.commit()

    update.message.reply_text(t(context, "lokatsiya_qabul"))
    update.message.reply_text(t(context, "royxatdan_otdi"))