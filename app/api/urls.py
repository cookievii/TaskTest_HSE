from api.views import StockViewSet, TradeViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = "api"

router_v1 = DefaultRouter()
router_v1.register("trades", TradeViewSet, basename="trades")
router_v1.register("stocks", StockViewSet, basename="stocks")


urlpatterns = [path("", include(router_v1.urls))]
