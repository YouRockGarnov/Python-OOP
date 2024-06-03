class Product:
    def __init__(self, product_id, name, description, price):
        raise NotImplementedError


class User:
    def __init__(self, user_id, first_name, last_name):
        raise NotImplementedError

    def add_to_cart(self, product):
        raise NotImplementedError

    def remove_from_cart(self, product_id):
        raise NotImplementedError


class Order:
    def __init__(self, order_id, user, products):
        raise NotImplementedError


class Marketplace:
    def __init__(self):
        raise NotImplementedError

    def add_product(self, product):
        raise NotImplementedError

    def remove_product(self, product_id):
        raise NotImplementedError

    def register_user(self, user):
        raise NotImplementedError

    def create_order(self, user_id):
        raise NotImplementedError

    def view_orders(self):
        raise NotImplementedError
