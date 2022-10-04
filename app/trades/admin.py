from django.contrib import admin

from trades.models import Trade


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "type",
        "user",
        "symbol",
        "price",
        "timestamp"
    )
    search_fields = ("type", "symbol")
