from api.repository import RepositoryTrade
from api.serializer import TradeSerializer
from core.views import UUIDModelViewSet


class TradeViewSet(UUIDModelViewSet):
    queryset = RepositoryTrade().get_all()
    serializer_class = TradeSerializer
