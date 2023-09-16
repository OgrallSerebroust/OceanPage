from django.db import models


class ProductType(models.Model):
    name = models.CharField(verbose_name="Название типа товара", max_length=256)

    class Meta:
        verbose_name = "Тип товаров"
        verbose_name_plural = "Типы товаров"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name="Название товара", max_length=256)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, verbose_name="Тип товара")
    photo = models.ImageField(verbose_name="Изображение товара", upload_to="productsImages/%Y/%m/%d/")
    description = models.TextField(verbose_name="Описание товара")
    country = models.CharField(verbose_name="Страна производитель", max_length=256)
    weight = models.FloatField(verbose_name="Примерный вес за единицу")
    price = models.DecimalField(verbose_name="Цена за единицу", max_digits=7, decimal_places=2)
    count = models.IntegerField(verbose_name="Остаток на складе")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name