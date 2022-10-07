from api.repository import UserRepository
from core.validators import (validate_queryset_after_filters,
                             validate_queryset_by_symbol, validate_user)
from django.db.models import Max, Min


class StockService:
    @staticmethod
    def get_queryset_by_symbol(qs, symbol):
        queryset = qs.filter(symbol=symbol)
        return queryset

    @staticmethod
    def filter_queryset_by_timestamp(queryset, time_start, time_end):
        queryset = queryset.filter(trade__timestamp__range=[time_start, time_end])
        return queryset

    @staticmethod
    def add_annotate_max_and_min(queryset):
        queryset = queryset.annotate(max=Max("trade__price"), min=Min("trade__price"))
        return queryset

    def make_filter_by_symbol_and_add_annotate(self, qs, symbol, start, end):
        get_queryset = self.get_queryset_by_symbol(qs, symbol)
        queryset_or_raise = validate_queryset_by_symbol(get_queryset, symbol)
        queryset_filter = self.filter_queryset_by_timestamp(
            queryset_or_raise, start, end
        )
        qs_or_raise_after_filter = validate_queryset_after_filters(queryset_filter)
        queryset_add_annotate = self.add_annotate_max_and_min(qs_or_raise_after_filter)
        return queryset_add_annotate.first()


class UserService:
    @staticmethod
    def get_user_by_id_and_name(id, name):
        user = UserRepository().get_obj_by_id_and_name(id=id, name=name)
        return user

    def get_user(self, id, name):
        get_user = self.get_user_by_id_and_name(id, name)
        valid_user_or_raise = validate_user(get_user, id, name)
        return valid_user_or_raise
