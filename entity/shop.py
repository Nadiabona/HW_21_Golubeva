from entity.base_storage import BaseStorage
from entity.exceptions import TooManyDifferentItemsError


class Shop(BaseStorage):
    def __init__(self, items: dict, capacity: int = 20): #we rewrite constructor to manage the input parameters
        super().__init__(items, capacity)

    #we need to rewrite this method beacuse of the confition of 5 different items for the shop
    def add(self, name: str, amount: int) -> None:
        if self.get_unique_items_count() >= 5:
            raise TooManyDifferentItemsError

        super().add(name, amount)



