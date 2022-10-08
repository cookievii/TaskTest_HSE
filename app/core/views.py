from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin, RetrieveModelMixin)
from rest_framework.viewsets import GenericViewSet


class UUIDModelViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    """Абстрактный ViewSet для таблиц с полями uuid."""

    lookup_field = "id"
