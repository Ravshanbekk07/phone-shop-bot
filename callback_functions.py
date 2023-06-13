from telegram import (
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import CallbackContext
from db import DB

db = DB(file_name='db.json')


def start(update: Update, context: CallbackContext) -> None:
   

    btn1= InlineKeyboardButton(text = "mavjud brendlar", callback_data="mavjud brendlar")
    

    inline_keyboard = [[btn1]]

    # get first name
    first_name = update.message.chat.first_name

    # send message with two buttons
    update.message.reply_html(
        text=f"Hello, <b>{first_name}</b>. Xush Kelibsiz \n Bu-Telefon savdo \n Sahifani tanlang 👇🏼",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    )

def brands(update: Update, context: CallbackContext):
    inline_keyboards = []
    for brend in db.get_brends():
        btn1 = InlineKeyboardButton(text=brend , callback_data=f"brend:{brend}")
        inline_keyboards.append([btn1])

    update.callback_query.message.reply_text(
        text = f"bizda mavjud brendlar quyidagilar ⏬",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboards)
    )

def send_products(update: Update, context: CallbackContext):
    brend = update.callback_query.data.split(":")[1]
    products = db.get_phones_by_brend(brend)
    inline_keyboards = []
    for product in products:
        btn1 = InlineKeyboardButton(text=product['name'] , callback_data=f"product:{product.doc_id}")
        inline_keyboards.append([btn1])

    update.callback_query.message.reply_text(
        text = f"bizda {brend} brendiga tegishli mahsulotlar quyidagilar ⏬",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboards)
    )

def send_product_detail(update: Update, context: CallbackContext):
    product_id = int(update.callback_query.data.split(":")[1])
    product = db.get_phones_by_id(product_id)
    update.callback_query.message.reply_photo(
        photo=product['image'],
        caption = f"bizda {product['name']} mahsuloti quyidagilar ⏬\n\nbrendi: {product['brend']}\nrang: {product['color']}\nram: {product['ram']}\nxotira: {product['memory']}\nnarxi: {product['price']}"
        # reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboards)
    )

    