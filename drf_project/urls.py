from django.contrib import admin
from django.urls import path
from core.views import IndexAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexAPI.as_view(), name = "index"),
]
