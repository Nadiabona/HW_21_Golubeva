from entity.abstract_storage import AbstractStorage
from collections import defaultdict

from entity.exceptions import NotEnoughSpaceError, UnknownProductError, NotEnoughProductError


class BaseStorage(AbstractStorage):
    def __init__(self, items : dict, capacity : int):
        self._items = items
        #self._items = defaultdict(int)
        self._capacity = capacity

    def add(self, name, amount) -> None:

        if self.get_free_space() < amount:
            raise NotEnoughSpaceError
        # if name in self._items:
        #     self._items[name] += amount
        # else:
        #     self._items[name] = amount

        self._items[name] = self._items.get(name, 0) + amount

    def remove(self, name: str, amount: int) -> None:
        if name not in self._items:
            raise UnknownProductError

        if self._items[name] < amount:
            raise NotEnoughProductError

        self._items[name] -= amount
        if self._items[name]==0:
            self._items.pop(name)

    def get_free_space(self) -> int:
        return self._capacity - sum(self._items.values())

    def get_items(self) -> dict:
        return self._items

    def get_unique_items_count(self) -> int:
        return len(self._items)




