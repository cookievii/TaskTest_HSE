from api.repository import RepositoryStock, RepositoryTrade
from rest_framework import serializers
from api.repository import RepositoryUser
from app.settings import DATETIME_FORMAT
from core.validators import validate_symbol, validate_user_name


class SimpleStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepositoryStock.model
        fields = ("symbol",)
        lookup_field = 'symbol'
        extra_kwargs = {
            'url': {'lookup_field': 'symbol'}
        }


class StockSerializer(SimpleStockSerializer):
    max = serializers.SerializerMethodField()
    min = serializers.SerializerMethodField()

    class Meta:
        model = RepositoryStock.model
        fields = ("symbol", "max", "min")

    def get_max(self, obj):
        return obj.max

    def get_min(self, obj):
        return obj.min


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepositoryUser.model
        fields = ("id", "name")


class TradeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    symbol = serializers.PrimaryKeyRelatedField(
        read_only=True,
        source="stock.symbol")
    timestamp = serializers.DateTimeField(format=DATETIME_FORMAT)

    class Meta:
        model = RepositoryTrade.model
        fields = ("id", "type", "user", "symbol", "price", "timestamp")

    def create(self, validated_data):
        get_user_name = self.initial_data.get("user").get("name")
        validated_user_name = validate_user_name(get_user_name)
        user = RepositoryUser().get_or_create(name=validated_user_name)

        get_symbol = self.initial_data.get("symbol")
        validated_symbol = validate_symbol(get_symbol)
        stock = RepositoryStock().get_or_create(symbol=validated_symbol)

        trade = RepositoryTrade().get_or_create(
            user=user, stock=stock, **validated_data)

        return trade
