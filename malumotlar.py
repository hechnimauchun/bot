from db import *
from translations import t

def malumotlarim(update, context):
    user_id = update.effective_user.id
    cursor.execute("SELECT ism, familiya, tel_nomer, lokatsiya FROM users WHERE user_id=?", (user_id,))
    malumot = cursor.fetchone()
    if malumot:
        ism, familiya, tel_nomer, lokatsiya = malumot
        update.message.reply_text(
            f"{t(context, 'ism_tugma')}: {ism}\n"
            f"{t(context, 'familiya_tugma')}: {familiya}\n"
            f"{t(context, 'tel_tugma')}: {tel_nomer}\n"
            f"{t(context, 'lokatsiya_tugma')}: {lokatsiya}"
        )
    else:
        update.message.reply_text(t(context, "malumot_topilmadi"))