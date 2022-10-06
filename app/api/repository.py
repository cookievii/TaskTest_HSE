from django.db.models import Count
from django.db.models import Max, Min
from core.validators import validate_queryset_after_filters
from core.validators import validate_queryset_by_symbol
from trades.models import Stock
from trades.models import Trade, User


class RepositoryStock:
    model = Stock
    objects = model.objects.prefetch_related("trade")

    @staticmethod
    def add_annotate_max_and_min(queryset):
        return queryset.annotate(
            max=Max("trade__price"),
            min=Min("trade__price"),
            count=Count("trade__id")
        )

    def get_all(self):
        return self.objects.all()

    def get_queryset_by_symbol(self, symbol):
        get_queryset = self.objects.filter(symbol=symbol)
        queryset = validate_queryset_by_symbol(get_queryset, symbol)
        return queryset

    def get_or_create(self, **validate_data):
        obj, created_new_obj = self.objects.get_or_create(**validate_data)
        if created_new_obj:
            obj.save()
            return obj
        return obj

    def filter_queryset_by_timestamp(self, queryset, start, end):
        queryset = queryset.filter(trade__timestamp__range=[start, end])
        queryset = validate_queryset_after_filters(queryset)
        return queryset


class RepositoryUser(RepositoryStock):
    model = User
    objects = model.objects


class RepositoryTrade(RepositoryStock):
    model = Trade
    objects = model.objects.select_related("stock").select_related("user")

