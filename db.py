from tinydb import TinyDB, Query
from tinydb.table import Document


class DB:
    def __init__(self, file_name: str) -> None:
        '''create tinydb as attribute'''
        db = TinyDB(file_name, indent=4)
        self.phones = db.table('phones')
        self.users = db.table('users')
        self.cart = db.table('cart')

    def add_phone(
        self, 
        name: str, 
        brend: str, 
        color: str, 
        ram: int, 
        memory: int, 
        price: float, 
        image: str) -> int:
        '''
        Insert a new phone into the database.

        :params: the document's cloumn name
        :returns: the inserted document's ID
        '''
        data = {
            "name": name,
            "brend": brend,
            "color": color,
            "ram": ram,
            "memory": memory,
            "price": price,
            "image": image
        }
        return self.phones.insert(data)

    def is_user(self, chat_id: str) -> bool:
        '''chack is user'''
        return self.users.contains(doc_id=chat_id)

    def is_phone(self, phone_id: str) -> bool:
        '''chack is user'''
        return self.phones.contains(doc_id=phone_id)

    def get_brends(self) -> bool:
        '''chack is user'''
        brends = []
        for phone in self.phones.all():
            if phone['brend'] not in brends:
                brends.append(phone['brend'])

        return brends

    def get_phones_by_brend(self, brend: str) -> bool:
        '''chack is user'''
        return self.phones.search(cond=Query().brend==brend)

    def get_phones_by_id(self, phone_id: str) -> bool:
        '''chack is user'''
        return self.phones.get(doc_id=phone_id)

    def add_user(self, chat_id: str, first_name: str, last_name=None, username=None) -> int:
        '''
        add a new user into the users table.

        params: users data
        returns: doc id
        '''
        if self.is_user(chat_id=chat_id):
            return False

        doc = Document(
            {
                'first_name': first_name,
                'last_name': last_name,
                'username': username
            },
            doc_id=chat_id)
        return self.users.insert(doc)

    def add_cart(self, user_id: str, phone_id: str) -> int:
        '''
        add a new cart into the cart table.

        params: cart data
        returns: doc id
        '''
        if self.is_user(chat_id=user_id) and self.is_phone(phone_id=phone_id):
            return self.cart.insert({'user_id': user_id, "phone_id": phone_id})
        return False

    def remove_cart(self, cart_id) -> bool:
        '''
        remove cart into the cart table.

        params: cart data
        returns: doc id
        '''
        return self.cart.remove(doc_ids=[cart_id])
    
    def clear_cart(self, user_id: str) -> bool:
        '''
        clear cart.
        '''
        return self.cart.remove(cond=(Query().user_id==user_id))
    
    def get_my_cart(self, user_id: str) -> bool:
        '''
        clear cart.
        '''
        return self.cart.search(cond=(Query().user_id==user_id))