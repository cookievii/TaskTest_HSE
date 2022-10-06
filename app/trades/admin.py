from django.contrib import admin

from api.repository import RepositoryStock, RepositoryTrade, RepositoryUser


@admin.register(RepositoryUser.model)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "pkid",
        "id",
        "name"
    )
    search_fields = ("name",)


@admin.register(RepositoryStock.model)
class StockAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "symbol"
    )
    search_fields = ("symbol",)


@admin.register(RepositoryTrade.model)
class TradeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "type",
        "user",
        "stock",
        "price",
        "timestamp"
    )
    search_fields = ("type",)
