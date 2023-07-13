from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(route="catalog/", view=views.catalog, name="catalog"),
]
