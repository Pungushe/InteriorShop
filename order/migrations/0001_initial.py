# Generated by Django 4.2.4 on 2023-08-18 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('zipcode', models.CharField(max_length=100, verbose_name='Индекс')),
                ('place', models.CharField(max_length=100, verbose_name='Город')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Оплачено')),
                ('vendors', models.ManyToManyField(related_name='orders', to='vendor.vendor', verbose_name='Продавец')),
            ],
            options={
                'verbose_name_plural': 'Заказы',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_paid', models.BooleanField(default=False, verbose_name='Оплачен продавцом')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена')),
                ('quantity', models.IntegerField(default=1, verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='product.product', verbose_name='Товар')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='vendor.vendor', verbose_name='Продавец')),
            ],
            options={
                'verbose_name_plural': 'Товары заказа',
            },
        ),
    ]
