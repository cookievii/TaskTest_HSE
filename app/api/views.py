from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from api.repository import RepositoryStock
from api.repository import RepositoryTrade
from api.serializers import SimpleStockSerializer
from api.serializers import StockSerializer
from api.serializers import TradeSerializer
from api.services import StockService
from core.filters import TradeFilter
from core.views import UUIDModelViewSet


class TradeViewSet(UUIDModelViewSet):
    queryset = RepositoryTrade().get_all()
    serializer_class = TradeSerializer
    filterset_class = TradeFilter


class StockViewSet(UUIDModelViewSet):
    queryset = RepositoryStock().get_all()
    serializer_class = SimpleStockSerializer
    lookup_field = 'symbol'

    @action(methods=["get"], detail=True, url_path="price", url_name="price")
    def price(self, request, symbol=None):
        queryset = StockService().make_filter_by_symbol_and_add_annotate(
            qs=self.queryset,
            symbol=symbol,
            start=request.query_params.get("start", "0001-01-01"),
            end=request.query_params.get("end", "9999-01-01"))
        serializers = StockSerializer(queryset, many=False)
        return Response(serializers.data, status=HTTP_200_OK)
