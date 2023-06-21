import os
from telegram.ext import (
    CommandHandler,
    MessageHandler, Filters,
    CallbackQueryHandler,
    Dispatcher
)
from callback_functions import (
    start, brands,
    send_products, send_product_detail,remove,add_cart,my_cards,kontaktlar,haqimizda,clear

)
from telegram import Bot,Update
from flask import Flask,request
from db import DB

app = Flask(__name__)

TOKEN = os.environ.get('TOKEN')
bot = Bot(TOKEN)

db = DB(file_name='db.json')

@app.route('/webhook/',methods = ['POST'])
def main():
    
    dispatcher = Dispatcher(bot,None,workers =0)
    data = request.get_json(force=True)
    update = Update.de_json(data=data,bot=bot)

    dispatcher.add_handler(handler=CommandHandler('start', start))
    dispatcher.add_handler(handler=CallbackQueryHandler(send_products, pattern="brend:"))
    dispatcher.add_handler(handler=CallbackQueryHandler(send_product_detail, pattern="product:"))
    dispatcher.add_handler(handler=CallbackQueryHandler(remove, pattern="remove"))
    dispatcher.add_handler(handler=CallbackQueryHandler(add_cart,pattern='add-cart:'))
    dispatcher.add_handler(handler=CallbackQueryHandler(clear, pattern="clear cart"))

    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text('📓mavjud brendlar'), callback=brands)) 
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text('🛒my cart'), callback=my_cards))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text('☎️contact'),callback = kontaktlar))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text('📝about'),callback = haqimizda))
    
    dispatcher.process_update(update)
    return 'cool'

@app.route('/')
def home():
    return 'running'

@app.route('/set-webhook/')
def set_hook():

    r = bot.set_webhook("https://stanger.pythonanywhere.com/webhook/")
    return f'info:{r}'

