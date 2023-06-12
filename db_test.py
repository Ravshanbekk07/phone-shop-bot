from tinydb import TinyDB
from db import DB
import random

db = DB('db.json')


def test_add_phone():
    demo = TinyDB('demo-db.json')

    rams = [2, 3, 4, 6, 8, 12]
    memmoris = [16, 32, 64, 124, 256, 512]

    for table in demo.tables():
        for phone in demo.table(table).all():
            doc_id = db.add_phone(
                name=phone['name'],
                brend=phone['company'],
                color=phone['color'],
                ram=random.choice(rams),
                memory=random.choice(memmoris),
                price=phone['price'],
                image=phone['img_url'])

            print(doc_id)


def test_add_user(chat_id: str, first_name: str, last_name: str, username: str):
    db.add_user(chat_id=chat_id, first_name=first_name, last_name=last_name, username=username)


def test_add_cart():
    print(db.add_cart('5436234', '4'))


def test_remove_cart():
    db.remove_cart(cart_id=4)

def test_clear_cart():
    db.clear_cart("654367252")

def test_get_brends():
    print(db.get_brends())

def test_get_phone_by_brend(brend):
    print(db.get_phones_by_brend(brend))

# test_get_phone_by_brend('Samsung')