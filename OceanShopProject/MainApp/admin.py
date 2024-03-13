from django.contrib import admin
from .models import MainPageTexts, ProductType, Product, OtherPages


class MainPageTextsAdmin(admin.ModelAdmin):
    list_display = ["description", "id"]


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "product_type"]
    list_filter =["product_type"]


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(MainPageTexts, MainPageTextsAdmin)
admin.site.register(OtherPages)
