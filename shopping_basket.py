
from dataclasses import dataclass
from item import Item
@dataclass
class Basket(object):
    items: List[Item]

    def total(self):
        if len(self.items) > 0:
            return self.items[0].unit_price
        return 0


if __name__ == "__main__":
    pass