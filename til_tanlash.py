import time
from royxatdan_ot import royxatdan_ot
from translations import t

def til_tanlash(update, context):
    query = update.callback_query
    query.answer()
    chat_id = update.effective_chat.id

    if query.data in ("uz", "ru", "en"):
        context.user_data['til'] = query.data
        query.delete_message()
        msg1 = context.bot.send_message(chat_id=chat_id, text="⌛")
        time.sleep(3)
        msg1.delete()
        context.bot.send_message(chat_id=chat_id, text=t(context, "til_tanlandi"))
        time.sleep(2)
        royxatdan_ot(update, context)