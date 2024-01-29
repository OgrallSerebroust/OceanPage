from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(route="catalog", view=views.catalog, name="catalog"),
    path(route="contacts/", view=views.contacts, name="contacts"),
    path(route="delivery/", view=views.delivery, name="delivery"),
    url(r'^search/$', view=views.search, name="search")
]
