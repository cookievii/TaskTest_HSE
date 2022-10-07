from trades.models import Stock
from trades.models import Trade, User


class RepositoryStock:
    model = Stock
    objects = model.objects

    def get_all(self):
        return self.objects.all()

    def get_or_create(self, **validate_data):
        obj, created_new_obj = self.objects.get_or_create(**validate_data)
        return obj


class RepositoryUser(RepositoryStock):
    model = User
    objects = model.objects


class RepositoryTrade(RepositoryStock):
    model = Trade
    objects = model.objects.select_related("stock").select_related("user")

