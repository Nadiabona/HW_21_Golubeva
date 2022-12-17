from entity.courier import Courier
from entity.exceptions import BaseError
from entity.request import Request
from entity.shop import Shop
from entity.store import Store

shop = Shop(
    items = {'печенька' : 3,
             'ноутбук' : 1,
             'кот' : 1,
             'собака' : 3,

             }
)
store = Store(
    items = {'печенька' : 10,
             'конфетка' : 20,

             }
)
storages = {
    'магазин': shop,
    'склад': store,
}
def main():
    while True:
        for storage_name in storages:
            print(f'В {storage_name} хранится: {storages[storage_name].get_items()}')
            print(f' Cвободное место: {storages[storage_name].get_free_space()}')

        user_input = input('Введите строку в формате "Доставить 3 печенька из склада в магазин".\n'
                           'Введите "стоп" или "stop", чтобы продолжить:\n',                       )
        if user_input in ("stop", "стоп"):
            break


        try:
            request = Request(request_str = user_input, storages = storages)
            courier = Courier(request=request, storages=storages)
            courier.move()

        except BaseError as error: #забираем объект ошибки
            print(error.message)



if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
