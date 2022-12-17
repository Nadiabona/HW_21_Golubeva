from typing import Dict

from entity.abstract_storage import AbstractStorage
from entity.exceptions import NotEnoughSpaceError, TooManyDifferentItemsError
from entity.request import Request
from entity.shop import Shop
from entity.store import Store

# shop_1 = Shop(
#     items = {'печенька' : 3,
#              'ноутбук' : 15,
#
#
#              }
# )
#
# store_1 = Store(
#     items = {'печенька' : 10,
#              'ноутбук' : 20
#              }
# )
# storages_1 = {
#     'магазин': shop_1,
#     'склад': store_1,
# }

class Courier:
    def __init__(self, request: Request, storages : Dict[str, AbstractStorage]):
        self.request = request

        self.from_where: AbstractStorage = storages[self.request.departure]
        self.to_where: AbstractStorage = storages[self.request.destination]


    def move(self):
        if self.to_where.get_free_space() < self.request.amount:
            raise NotEnoughSpaceError
        elif self.to_where.get_unique_items_count()==4 \
                and self.request.product not in self.to_where.get_items().keys():

            raise TooManyDifferentItemsError

        self.from_where.remove(name = self.request.product, amount = self.request.amount)
        print(f'Курьер забрал {self.request.amount} {self.request.product} из {self.request.departure} ')

        print(f'Курьер везет {self.request.amount} {self.request.product}')

        self.to_where.add(name = self.request.product, amount = self.request.amount)
        print(f"Курьер доставил {self.request.amount} {self.request.product} в {self.request.destination}")

# test_str = "Доставь 3 печенька из склад в магазин"
# test_request = Request(test_str, storages_1)
# test_courier = Courier(test_request, storages_1 )
# print(test_request.product)
# # print(test_courier.to_where())
# # test_courier = Courier(test_request, storages_1 )
# # print (test_courier.from_where.get_free_space())
# print (test_courier.from_where.get_items().keys())
# # print (test_courier.from_where.get_unique_items_count())
# print(test_request.product in test_courier.from_where.get_items().keys() )