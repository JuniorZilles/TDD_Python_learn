import unittest

from item import Item
from shopping_basket import Basket



class ShoppingBasket(unittest.TestCase):
    def test_empty_basket_total(self):
        basket = Basket([])
        self.assertEqual(basket.total(), 0)

    def test_text_single_item_quantity(self):
        basket = Basket([Item(100.0, 1)])
        self.assertEqual(basket.total(), 100.0)
        