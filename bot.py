import os
from telegram.ext import (
    Updater, CommandHandler,
    MessageHandler, Filters,
    CallbackQueryHandler,
)
from callback_functions import (
    start, brands,
    send_products, send_product_detail,
)

TOKEN = os.environ.get('TOKEN')


def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(handler=CommandHandler('start', start))
    dispatcher.add_handler(handler=CallbackQueryHandler(
        brands, pattern="mavjud brendlar"))
    dispatcher.add_handler(handler=CallbackQueryHandler(
        send_products, pattern="brend:"))
    dispatcher.add_handler(handler=CallbackQueryHandler(
        send_product_detail, pattern="product:"))

    updater.start_polling()
    updater.idle()


main()
