from api.repository import StockRepository, TradeRepository, UserRepository
from api.services import UserService
from core.validators import validate_symbol
from rest_framework import serializers

from app.settings import DATETIME_FORMAT


class SimpleStockSerializer(serializers.ModelSerializer):
    """Сериализатор таблицы Stock."""

    class Meta:
        model = StockRepository.model
        fields = ("symbol",)
        lookup_field = "symbol"
        extra_kwargs = {"url": {"lookup_field": "symbol"}}


class StockSerializer(SimpleStockSerializer):
    """Расщиренный сериализатор таблицы Stock."""

    max = serializers.SerializerMethodField()
    min = serializers.SerializerMethodField()

    class Meta:
        model = StockRepository.model
        fields = ("symbol", "max", "min")

    def get_max(self, obj):
        """Возвращает annotate поле 'max'."""
        return obj.max

    def get_min(self, obj):
        """Возвращает annotate поле 'min'."""
        return obj.min


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор таблицы User."""

    name = serializers.CharField(source="username")

    class Meta:
        model = UserRepository.model
        fields = ("id", "name")


class TradeSerializer(serializers.ModelSerializer):
    """Сериализатор таблицы Trade."""

    user = UserSerializer(read_only=True)
    symbol = serializers.PrimaryKeyRelatedField(read_only=True, source="stock.symbol")
    timestamp = serializers.DateTimeField(format=DATETIME_FORMAT)

    class Meta:
        model = TradeRepository.model
        fields = ("id", "type", "user", "symbol", "price", "timestamp")

    def create(self, validated_data):
        """Создает новую запись Trade."""
        get_user_id = self.initial_data.get("user").get("id")
        get_user_name = self.initial_data.get("user").get("name")
        user = UserService().get_user_or_raise(get_user_id, get_user_name)

        get_symbol = self.initial_data.get("symbol")
        validated_symbol = validate_symbol(get_symbol)

        stock = StockRepository().get_or_create(symbol=validated_symbol)
        trade = TradeRepository().get_or_create(
            user=user, stock=stock, **validated_data
        )
        return trade
