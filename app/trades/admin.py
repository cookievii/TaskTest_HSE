from api.repository import StockRepository, TradeRepository, UserRepository
from django.contrib import admin


@admin.register(UserRepository.model)
class UserAdmin(admin.ModelAdmin):
    list_display = ("pkid", "id", "name")
    search_fields = ("name",)


@admin.register(StockRepository.model)
class StockAdmin(admin.ModelAdmin):
    list_display = ("id", "symbol")
    search_fields = ("symbol",)


@admin.register(TradeRepository.model)
class TradeAdmin(admin.ModelAdmin):
    list_display = ("id", "type", "user", "stock", "price", "timestamp")
    search_fields = ("type",)
