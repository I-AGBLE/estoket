from django.urls import path

from . import views


app_name = "app_users"
urlpatterns = [
    path("app_users/", views.index, name="index"),
    path("app_users/signup/", views.signup, name="signup"),
    path("app_users/profile/", views.profile, name="profile"),
    path("app_users/signup_continue/", views.signup_continue, name="signup_continue"),
    path("app_users/register_company/", views.register_company, name="register_company"),
]
