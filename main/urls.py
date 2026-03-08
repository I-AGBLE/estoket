from django.urls import path

from . import views


app_name = "market_place"
urlpatterns = [
    path("", views.index, name="index"),
]
