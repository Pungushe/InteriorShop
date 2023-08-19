from io import BytesIO
from django.utils.text import slugify
from PIL import Image

from django.core.files import File
from django.db import models

from vendor.models import Vendor


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0, verbose_name='Заказ')

    class Meta:
        ordering = ['ordering']
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='products', verbose_name='Продавец')
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255)
    description = models.TextField(verbose_name='Описание', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    date_added = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, verbose_name='Изображение')
    thumbnail=models.ImageField(upload_to='uploads/', blank=True, verbose_name='Миниатюра')

    class Meta:
        ordering = ['-date_added']
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='Товар')
    image = models.ImageField(upload_to='uploads/', null=True, blank=True, verbose_name='Изображение')
    thumbnail=models.ImageField(upload_to='uploads/', null=True, blank=True, verbose_name='Миниатюра')

    class Meta:
        verbose_name_plural = 'Изображения товара'

    def __str__(self):
        return self.title
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
