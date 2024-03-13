from django.db import models
from ckeditor.fields import RichTextField


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
    price_for_kg = models.BooleanField(verbose_name="Цена за килограмм", default=True)
    count = models.FloatField(verbose_name="Остаток на складе")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class MainPageTexts(models.Model):
    text = RichTextField(verbose_name="Текст для вывода")
    description = models.TextField(verbose_name="Описание", null=True, default=None)

    class Meta:
        verbose_name = "Текст для блока на основных страницах"
        verbose_name_plural = "Тексты для блоков на основных страницах"


class OtherPages(models.Model):
    title = models.CharField(verbose_name="Заголовок страницы", max_length=255)
    sub_title = models.CharField(verbose_name="Подпись под заголовком", max_length=255, null=True)
    content = RichTextField(verbose_name="Контент страницы")

    class Meta:
        verbose_name = "Второстепенная страница"
        verbose_name_plural = "Второстепенные страницы"
