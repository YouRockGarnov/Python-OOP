import pytest
from marketplace import Marketplace, Product, User


def test_marketplace():
    marketplace = Marketplace()

    product1 = Product("123", "Apple", "Fresh apple", 1.0)
    product2 = Product("456", "Banana", "Fresh banana", 0.5)

    user1 = User("789", "John", "Doe")
    user2 = User("012", "Jane", "Doe")

    marketplace.add_product(product1)
    marketplace.add_product(product2)
    marketplace.register_user(user1)
    marketplace.register_user(user2)

    user1.add_to_cart(product1)
    user2.add_to_cart(product2)
    user1.remove_from_cart("123")
    with pytest.raises(KeyError):
        user1.remove_from_cart("123")
    marketplace.remove_product("456")
    with pytest.raises(KeyError):
        marketplace.remove_product("456")

    user1.add_to_cart(product1)
    user2.add_to_cart(product2)

    marketplace.create_order("789")
    assert len(marketplace.view_orders()) == 1
    assert len(user1.cart) == 0

    order = marketplace.view_orders()[0]
    assert order.user == user1
    assert len(order.products) == 1
    assert "123" in order.products

    marketplace.create_order("012")
    assert len(marketplace.view_orders()) == 2
    assert len(user2.cart) == 0

    order = marketplace.view_orders()[1]
    assert order.user == user2
    assert len(order.products) == 1
    assert "456" in order.products
