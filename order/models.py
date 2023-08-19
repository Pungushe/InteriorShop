from django.db import models

from product.models import Product
from vendor.models import Vendor

class Order(models.Model):
    first_name=models.CharField(max_length=100, verbose_name="Имя")
    last_name=models.CharField(max_length=100, verbose_name="Фамилия")
    email=models.CharField (max_length=100)
    address=models.CharField(max_length=100, verbose_name="Адрес")
    zipcode=models.CharField(max_length=100, verbose_name="Индекс")
    place=models.CharField(max_length=100, verbose_name="Город")
    phone=models.CharField(max_length=100, verbose_name="Телефон")
    created_at=models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    paid_amount=models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Оплачено")
    vendors=models.ManyToManyField(Vendor, related_name='orders', verbose_name='Продавец')
    
    class Meta:
        ordering=["-created_at"]
        verbose_name_plural='Заказы'

    def __str__(self):
        return f"{self.first_name}"
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='Заказ')
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items', verbose_name='Товар')
    vendor=models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='items', verbose_name='Продавец')
    vendor_paid=models.BooleanField(default=False, verbose_name="Оплачен продавцом")
    price=models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    quantity=models.IntegerField(default=1, verbose_name="Количество")
    
    class Meta:
        verbose_name_plural='Товары заказа'

    def __str__(self):
        return f"{self.id}"
    
    def get_total_price(self):
        return self.price * self.quantity
    
