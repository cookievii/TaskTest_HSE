from importlib.resources import _

from api.repository import RepositoryTrade
from rest_framework import serializers

from api.repository import RepositoryUser
from core.validators import ValidateTrade


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = RepositoryUser.model
        fields = ("id", "name")


class TradeSerializer(serializers.ModelSerializer, ValidateTrade):
    user = UserSerializer()

    class Meta:
        model = RepositoryTrade.model
        fields = ("id", "type", "user", "symbol", "price", "timestamp")
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('type', 'user', "symbol", "price", "timestamp"),
                message=_("Trade already exists.")
            )
        ]



