from django.urls import path

from . import views


app_name = "public"
urlpatterns = [
    path("", views.index, name="index"),
    path("services/", views.all_services, name="all_services"),
    path("service/", views.service, name="service"),
    path("more_services/", views.more_services, name="more_services"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("company_services/", views.company_services, name="company_services"),
    path("company_expertise/", views.company_expertise, name="company_expertise"),
    path("company_links/", views.company_links, name="company_links"),
    path("edit_bio/", views.edit_bio, name="edit_bio"),
    path("service_form/", views.service_form, name="service_form"),
    path("add_expertise/", views.add_expertise, name="add_expertise"),
    path("add_faq/", views.add_faq, name="add_faq"),
    path("add_package/", views.add_package, name="add_package"),
]
