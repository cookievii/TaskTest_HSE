from trades.models import Stock, Trade, User


class StockRepository:
    """Методы взаимодействия с таблицей Stock."""

    model = Stock
    objects = model.objects

    def get_all(self) -> model:
        """Возвращает все записи из таблицы."""
        return self.objects.all()

    def get_or_create(self, **validate_data) -> model:
        """Возвращает объект из таблицы, если такой нет - создать новую."""
        obj, created_new_obj = self.objects.get_or_create(**validate_data)
        return obj


class UserRepository(StockRepository):
    """Методы взаимодействия с таблицей User."""

    model = User
    objects = model.objects

    def get_obj_by_id_and_name(self, id, name) -> model:
        """Возвращает объекты User по id и name."""
        return self.objects.filter(pkid=id, username=name)


class TradeRepository(StockRepository):
    """Методы взаимодействия с таблицей Trade."""

    model = Trade
    objects = model.objects.select_related("stock").select_related("user")
