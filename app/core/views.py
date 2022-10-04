from rest_framework.mixins import (CreateModelMixin, RetrieveModelMixin,
                                   DestroyModelMixin, ListModelMixin)
from rest_framework.viewsets import GenericViewSet


class UUIDModelViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin,
                       ListModelMixin, GenericViewSet):
    lookup_field = 'id'
