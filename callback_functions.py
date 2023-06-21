from telegram import (
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    KeyboardButton, ReplyKeyboardMarkup
)
from telegram.ext import CallbackContext
from db import DB

db = DB(file_name='db.json')


def start(update: Update, context: CallbackContext) -> None:

    db.add_user(update.message.chat.id,
                update.message.chat.first_name, update.message.chat.username)
    first_name = update.message.chat.first_name

    # btn1= InlineKeyboardButton(text = "mavjud brendlar", callback_data="mavjud brendlar")

    # inline_keyboard = [[btn1]]

    # # get first name

    # # send message with two buttons
    # update.message.reply_html(
    #     text=f"Hello, <b>{first_name}</b>. Xush Kelibsiz \n Bu-Telefon savdo \n Sahifani tanlang 👇🏼",
    #     reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

    btn1 = KeyboardButton("📓mavjud brendlar")
    btn2 = KeyboardButton('🛒my cart')
    btn3 = KeyboardButton('☎️contact')
    btn4 = KeyboardButton('📝about')

    reply_keyboard = [[btn1, btn2],
                      [btn3, btn4],

                      ]

    update.message.reply_html(
        text=f"Hello, <b>{first_name}</b>. Xush Kelibsiz \n Bu-Telefon savdo \n Sahifani tanlang 👇🏼",
        reply_markup=ReplyKeyboardMarkup(keyboard=reply_keyboard, resize_keyboard=True))


def brands(update: Update, context: CallbackContext):
    inline_keyboards = []
    for brend in db.get_brends():
        btn = InlineKeyboardButton(text=brend, callback_data=f"brend:{brend}")
        inline_keyboards.append([btn])
   
    update.message.reply_text(
        text=f"bizda mavjud brendlar quyidagilar ⏬",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboards)
    )


def send_products(update: Update, context: CallbackContext):
    brend = update.callback_query.data.split(":")[1]
    products = db.get_phones_by_brend(brend)
    inline_keyboards = []
    for product in products:
        btn1 = InlineKeyboardButton(
            text=product['name'], callback_data=f"product:{product.doc_id}")
        inline_keyboards.append([btn1])

    update.callback_query.message.reply_text(
        text=f"bizda {brend} brendiga tegishli mahsulotlar quyidagilar ⏬",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboards)
    )


def send_product_detail(update: Update, context: CallbackContext):

    product_id = int(update.callback_query.data.split(":")[1])
    btn1 = InlineKeyboardButton(
        text='add cart', callback_data=f'add-cart:{product_id}')
    btn2 = InlineKeyboardButton(text='remove', callback_data='remove')
    inline_keyboards = [[btn1, btn2]]
    product = db.get_phones_by_id(product_id)
    update.callback_query.message.reply_photo(
        photo=product['image'],
        caption=f"bizda {product['name']} mahsuloti quyidagilar ⏬\n\nbrendi: {product['brend']}\nrang: {product['color']}\nram: {product['ram']}\nxotira: {product['memory']}\nnarxi: {product['price']}",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboards)
    )


def remove(update: Update, context: CallbackContext):
    update.callback_query.message.delete()


def add_cart(update: Update, context: CallbackContext):
    chat_id = update.callback_query.message.chat.id
    product_id = update.callback_query.data.split(':')[1]
    db.add_cart(chat_id, product_id)
    update.callback_query.message.reply_text(
        text=f"savatga qoshildi ",

    )


def my_cards(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    products = db.get_my_cart(chat_id)

    text = ''
    for product_id in products:
        product = db.get_phones_by_id(product_id['phone_id'])
        text += f"brendi: {product['brend']}\nrang: {product['color']}\nram: {product['ram']}\nxotira: {product['memory']}\nnarxi: {product['price']}\n\n"
    btn1 = InlineKeyboardButton(text='clear cart', callback_data='clear cart')

    # create keyboard
    inline_keyboard = [[btn1]]

    if text == '':
        text = 'savatcha bosh'
    update.message.reply_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

    )


def clear(update: Update, context: CallbackContext):
    chat_id = update.callback_query.message.chat.id
    db.clear_cart(chat_id)
    update.callback_query.message.reply_text('savatcha tozalanadi')
    update.callback_query.message.delete()


def kontaktlar(update: Update, context: CallbackContext):
    btn1 = InlineKeyboardButton(text='instagram', url='https://instagram.com')
    btn2 = InlineKeyboardButton(text='kanal', url='https://t.me/Stranger070')
    btn3 = InlineKeyboardButton(
        text='boglanish', url='https://t.me/Stranger070')
    btn4 = InlineKeyboardButton(
        text='tavsiyalash', url='https://t.me/Stranger070')

    # create keyboard
    inline_keyboard = [[btn1, btn2], [btn3, btn4]]

    update.message.reply_html(
        text=f"<b>biz bilan boglanish uchun ⏬</b>",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    )


def haqimizda(update: Update, context: CallbackContext):
    update.message.reply_html(
        text=f"<b>Biz haqimizda: </b>\n biz <i>Phone shop</i> azolari ushbu botni\n 10.06.2023 da sizga manfaatli bolishi uchun tashkil qilganmiz.\n Biz orqali telefon sotib olganingizdan song\n bizni ozimiz sizga bonus sifatida dastavka xizmatlarini korsatamiz\n <b>faqatgina</b> siz 'contact' tugmasini bosib biz bilan aloqaga chiqishingiz darkor "

    )
