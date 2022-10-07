from core.models import UUIDModel
from django.db import models


class User(UUIDModel):
    name = models.CharField("Имя", max_length=150, unique=True)

    def __str__(self):
        return self.name


class Stock(models.Model):
    symbol = models.CharField(
        verbose_name="The stock symbol.", max_length=6, unique=True
    )

    def __str__(self):
        return self.symbol


class Trade(UUIDModel):
    __TYPE_CHOICES = (
        ("buy", "Buy"),
        ("sell", "Sell"),
    )
    type = models.CharField(
        verbose_name="The trade type.",
        choices=__TYPE_CHOICES,
        max_length=max([len(type_[0]) for type_ in __TYPE_CHOICES]),
    )
    user = models.ForeignKey(
        User,
        to_field="id",
        on_delete=models.CASCADE,
        related_name="trade",
        verbose_name="Deal owner.",
    )
    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
        related_name="trade",
        verbose_name="The stock symbol.",
    )
    price = models.DecimalField(
        verbose_name="The price of one share.", max_digits=19, decimal_places=2
    )
    timestamp = models.DateTimeField(
        verbose_name="Time of creation.", auto_created=True
    )

    def __str__(self):
        return f"{self.id} - {self.type}"
