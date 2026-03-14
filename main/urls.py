from django.urls import path

from . import views


app_name = "public"
urlpatterns = [
    path("", views.index, name="index"),
    path("services/", views.all_services, name="all_services"),
]
