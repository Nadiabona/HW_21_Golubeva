class BaseError(Exception):
    message = "Незвестная ошибка"

class NotEnoughSpaceError(BaseError):
    message = "Заказ неверный - в пункте назначения недостаточно места"

class UnknownProductError(BaseError):
    message = "Неизвестный товар"

class NotEnoughProductError(BaseError):
    message = "Недостаточно товара в пункте вывозза"

class InvalidRequestError(BaseError):
    message = "Неправильный запрос"

class UnknownStoreError(BaseError):
    message = "Неизвестный склад"

class TooManyDifferentItemsError(BaseError):
    message = "В пункте назначения будет слишком много разных товаров"
