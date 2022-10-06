from django_filters import CharFilter
from django_filters.rest_framework import FilterSet


class TradeFilter(FilterSet):
    user = CharFilter(method="filter_by_user_id")

    def filter_by_user_id(self, queryset, name, value):
        queryset = queryset.filter(user_id=value)
        return queryset
