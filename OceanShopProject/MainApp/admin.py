from django.contrib import admin
from .models import ProductType, Product


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "product_type"]
    list_filter =["product_type"]


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
