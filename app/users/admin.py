from api.repository import UserRepository
from django.contrib import admin


@admin.register(UserRepository.model)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "pkid", "id")
    search_fields = ("username",)
