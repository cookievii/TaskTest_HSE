import uuid

from django.db import models


class UUIDModel(models.Model):
    """Абстрактная модель для получения поля с 'uuid4'."""

    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True
