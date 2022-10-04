from django.contrib import admin
from django.urls import include
from django.urls import path

app_name = "app"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("api.urls", namespace="api"))
]
