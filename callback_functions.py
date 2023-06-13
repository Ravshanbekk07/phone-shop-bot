from telegram import (
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import CallbackContext



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
    btn1= InlineKeyboardButton(text = "Oppo" , callback_data="Oppo")
    btn2= InlineKeyboardButton(text =  "Xiaomi", callback_data="Xiaomi")
    btn3= InlineKeyboardButton(text = "Redmi", callback_data="Redmi")
    btn4= InlineKeyboardButton(text =  "Nokia",  callback_data="Nokia")
    btn5= InlineKeyboardButton(text = "Vivo" , callback_data="Vivo")
    btn6= InlineKeyboardButton(text =  "Huawei", callback_data="Huawei")
    btn7= InlineKeyboardButton(text = "Samsung", callback_data="Samsung")
    btn8= InlineKeyboardButton(text =  "Apple" , callback_data="Apple")
    btn9= InlineKeyboardButton(text =  "Mi",  callback_data="Mi")

    inline_key = [[btn1,btn2],[btn3,btn4],[btn5,btn6],[btn7,btn8],[btn9]]
    update.callback_query.message.reply_text(
        text = f"bizda mavjud brendlar quyidagilar ⏬",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_key)
    )
