from django.conf.urls import url
from . import views

app_name = "cart"

urlpatterns = [
    url(r'^$', views.cart_detail, name="cart_detail"),
    url(r'^add/(?P<product_id>\d+)/$', views.add_to_cart, name="add_to_cart"),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name="cart_remove")
]
