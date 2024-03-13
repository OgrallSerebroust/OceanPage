from django.db import models
from MainApp.models import Product


class Order(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=255)
    last_name = models.CharField(verbose_name="Фамилия", max_length=255)
    email = models.EmailField()
    address = models.CharField(verbose_name="Адрес", max_length=255)
    mobile_phone = models.CharField(verbose_name="Номер для связи", max_length=30, blank=False, null=True)
    # + created, updated, paid?

    class Meta:
        # ordering = ("-created")?
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self) -> str:
        return "Заказ {}".format(self.id)
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT ,related_name="items", verbose_name="Заказ")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="order_items", verbose_name="Продукт")
    price = models.DecimalField(verbose_name="Цена за единицу", max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name="Количество", default=1)

    def __str__(self) -> str:
        return "{}".format(self.id)
    
    def get_cost(self):
        return self.price * self.quantity
