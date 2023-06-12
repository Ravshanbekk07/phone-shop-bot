from tinydb import TinyDB


class DB:
    def __init__(self, file_name: str) -> None:
        '''create tinydb as attribute'''
        db = TinyDB(file_name, indent=4)
        self.phones = db.table('phones')
        self.users = db.table('users')
        self.cart = db.table('cart')

    