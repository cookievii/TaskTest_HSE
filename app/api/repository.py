from trades.models import Stock, Trade, User


class StockRepository:
    model = Stock
    objects = model.objects

    def get_all(self):
        return self.objects.all()

    def get_or_create(self, **validate_data):
        obj, created_new_obj = self.objects.get_or_create(**validate_data)
        return obj


class UserRepository(StockRepository):
    model = User
    objects = model.objects

    def get_obj_by_id_and_name(self, id, name):
        return self.objects.filter(pkid=id, username=name)


class TradeRepository(StockRepository):
    model = Trade
    objects = model.objects.select_related("stock").select_related("user")
