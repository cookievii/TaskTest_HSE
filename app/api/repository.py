from trades.models import Trade, User


class RepositoryUser:
    model = User

    def get_all(self):
        return self.model.objects.all()

    def get_or_create(self, pkid, name):
        user, created_new_user = self.model.objects.get_or_create(
            pkid=pkid,
            name=name
        )
        if created_new_user:
            user.save()
        return user


class RepositoryTrade:
    model = Trade

    def get_all(self):
        return self.model.objects.all()

    def create_new(self, **validate_data):
        return self.model.objects.create(**validate_data)

    def objects_exists(self, type, user, symbol, price, timestamp):
        exists = self.model.objects.filter(
            type=type,
            user=user,
            symbol=symbol,
            price=price,
            timestamp=timestamp
        ).exists()
        return exists
