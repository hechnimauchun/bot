from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from til_tanlash import til_tanlash
from config import bot_token
from start import start
from royxatdan_ot import royxatdan_ot, ism, familiya, tel_nomer, lokatsiya, matn_qabul
from malumotlar import malumotlarim

def main():
    updater = Updater(token=bot_token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("malumotlarim", malumotlarim))
    dispatcher.add_handler(CallbackQueryHandler(til_tanlash))
    dispatcher.add_handler(MessageHandler(Filters.regex("^(ISM|ИМЯ|FIRST NAME)$"), ism))
    dispatcher.add_handler(MessageHandler(Filters.regex("^(FAMILIYA|ФАМИЛИЯ|LAST NAME)$"), familiya))
    dispatcher.add_handler(MessageHandler(Filters.contact, tel_nomer))
    dispatcher.add_handler(MessageHandler(Filters.location, lokatsiya))
    dispatcher.add_handler(MessageHandler(Filters.regex("^(MA'LUMOTLARIM|МОИ ДАННЫЕ|MY DATA)$"), malumotlarim))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, matn_qabul))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()