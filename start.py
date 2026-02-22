import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start(update, context):
    tillar = [
        [
            InlineKeyboardButton("O'ZBEKCHA" , callback_data="uz")
        ],
        [
            InlineKeyboardButton("INGLIZCHA" , callback_data="en")
        ],
        [
            InlineKeyboardButton("RUSCHA" , callback_data="ru")
        ]
    ]
    update.message.reply_text("TILNI TANLANG\nВЫБЕРИТЕ ЯЗЫК\nCHOOSE LANGUAGE", reply_markup=InlineKeyboardMarkup(tillar))
