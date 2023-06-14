import os
from telegram.ext import (
    Updater, CommandHandler,
    MessageHandler, Filters,
    CallbackQueryHandler,
)
from callback_functions import (
    start, brands,
    send_products, send_product_detail,remove,add_cart,my_cards,kontaktlar,haqimizda,clear

)

TOKEN = os.environ.get('TOKEN')


def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(handler=CommandHandler('start', start))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text('📓mavjud brendlar'), callback=brands)) 
    dispatcher.add_handler(handler=CallbackQueryHandler(send_products, pattern="brend:"))
    dispatcher.add_handler(handler=CallbackQueryHandler(send_product_detail, pattern="product:"))
    dispatcher.add_handler(handler=CallbackQueryHandler(remove, pattern="remove"))
    dispatcher.add_handler(handler=CallbackQueryHandler(add_cart,pattern='add-cart:'))
    dispatcher.add_handler(handler=CallbackQueryHandler(clear, pattern="clear cart"))

    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text('🛒my cart'), callback=my_cards))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text('☎️contact'),callback = kontaktlar))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text('📝about'),callback = haqimizda))
    

    updater.start_polling()
    updater.idle()
main()
