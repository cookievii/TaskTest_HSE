from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_400_BAD_REQUEST

from api.repository import RepositoryStock as RS
from api.repository import RepositoryTrade
from api.serializer import SimpleStockSerializer
from api.serializer import StockSerializer
from api.serializer import TradeSerializer
from core.filters import TradeFilter
from core.views import UUIDModelViewSet


class TradeViewSet(UUIDModelViewSet):
    queryset = RepositoryTrade().get_all()
    serializer_class = TradeSerializer
    filterset_class = TradeFilter


class StockViewSet(UUIDModelViewSet):
    queryset = RS().get_all()
    serializer_class = SimpleStockSerializer
    lookup_field = 'symbol'
    filterset_class = None

    @action(methods=["get"], detail=True, url_path="price", url_name="price")
    def price(self, request, symbol=None):
        get_queryset = RS().get_queryset_by_symbol(symbol)
        start = request.query_params.get("start", "0001-01-01")
        end = request.query_params.get("end", "9999-01-01")
        queryset = RS().filter_queryset_by_timestamp(get_queryset, start, end)
        queryset = RS().add_annotate_max_and_min(queryset)
        serializers = StockSerializer(queryset.first(), many=False)
        return Response(serializers.data, status=HTTP_200_OK)
