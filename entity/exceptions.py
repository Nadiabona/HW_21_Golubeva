class BaseError(Exception):
    message = "Незвестная ошибка"

class NotEnoughSpaceError(BaseError):
    message = "Недостаточно места"

class UnknownProductError(BaseError):
    message = "Неизвестный товар"

class NotEnoughProductError(BaseError):
    message = "Недостаточно товара"

class InvalidRequestError(BaseError):
    message = "Неправильный запрос"

class UnknownStoreError(BaseError):
    message = "Неизвестный склад"

class TooManyDifferentItemsError(BaseError):
    message = "Слишком много разных товаров"
