import os
from telegram.ext import (
    Updater, CommandHandler,
    MessageHandler, Filters,

    CallbackQueryHandler,
)
from callback_functions import (
    start,brands

)
from db import DB,get_phones_by_brend
db = DB(file_name='db.json')

TOKEN = os.environ.get('TOKEN')


def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(handler=CommandHandler('start',start))
    dispatcher.add_handler(handler=CallbackQueryHandler(brands, pattern = "mavjud brendlar"))
    dispatcher.add_handler(handler=CallbackQueryHandler(db.get_phones_by_brend, pattern = "Oppo"))
    dispatcher.add_handler(handler=CallbackQueryHandler(get_phones_by_brend, pattern = "Vivo"))
    dispatcher.add_handler(handler=CallbackQueryHandler(get_phones_by_brend, pattern = "Huawei"))
    dispatcher.add_handler(handler=CallbackQueryHandler(get_phones_by_brend, pattern = "Samsung"))
    dispatcher.add_handler(handler=CallbackQueryHandler(get_phones_by_brend, pattern = "Apple"))
    dispatcher.add_handler(handler=CallbackQueryHandler(get_phones_by_brend, pattern = "Nokia"))
    dispatcher.add_handler(handler=CallbackQueryHandler(get_phones_by_brend, pattern = "Mi"))
    dispatcher.add_handler(handler=CallbackQueryHandler(get_phones_by_brend, pattern = "Redmi"))
    dispatcher.add_handler(handler=CallbackQueryHandler(get_phones_by_brend, pattern = "Xiaomi"))



    updater.start_polling()
    updater.idle()

main()






