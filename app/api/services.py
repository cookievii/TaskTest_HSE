from api.repository import UserRepository
from core.validators import (validate_queryset_after_filters,
                             validate_queryset_by_symbol, validate_user)
from django.db.models import Max, Min


class StockService:
    """Логика работы с объектами Stock."""

    @staticmethod
    def filter_queryset_by_symbol(queryset, symbol):
        """Возвращает отфильтрованный 'queryset' по полю 'symbol'."""
        queryset = queryset.filter(symbol=symbol)
        return queryset

    @staticmethod
    def filter_queryset_by_timestamp(queryset, time_start, time_end):
        """Возвращает отфильтрованный 'queryset' по полю 'timestamp',
        таблицы 'Trade'."""
        queryset = queryset.filter(trade__timestamp__range=[time_start, time_end])
        return queryset

    @staticmethod
    def add_annotate_max_and_min(queryset):
        """Возвращает queryset с annotate полями:
        max - Получить максимальный 'price',
        min - Получить минимальный 'price'."""
        queryset = queryset.annotate(max=Max("trade__price"), min=Min("trade__price"))
        return queryset

    def make_filter_by_symbol_and_add_annotate(self, qs, symbol, start, end):
        """Возвращает отфильтрованный Stock с полями 'max' и 'min'."""
        get_queryset = self.filter_queryset_by_symbol(qs, symbol)
        queryset_or_raise = validate_queryset_by_symbol(get_queryset, symbol)
        queryset_filter = self.filter_queryset_by_timestamp(
            queryset_or_raise, start, end
        )
        queryset_or_raise_after_filter = validate_queryset_after_filters(
            queryset_filter
        )
        queryset_add_annotate = self.add_annotate_max_and_min(
            queryset_or_raise_after_filter
        )
        return queryset_add_annotate.first()


class UserService:
    """Логика работы с объектами User."""

    @staticmethod
    def get_user_by_id_and_name(id, name):
        """Возвращает User по 'id' и 'name'."""
        user = UserRepository().get_obj_by_id_and_name(id=id, name=name)
        return user

    def get_user_or_raise(self, id, name):
        """Возвращает User по 'id' и 'name' или вызвать raise."""
        get_user = self.get_user_by_id_and_name(id, name)
        valid_user_or_raise = validate_user(get_user, id, name)
        return valid_user_or_raise
