from django.urls import path

from . import views


app_name = "app_users"
urlpatterns = [
    path("app_users/", views.index, name="index"),
    path("app_users/signup/", views.signup, name="signup"),
]
