# coding: utf-8
from datetime import datetime

from django.db import models

class Product(models.Model):
    title = models.CharField(
        verbose_name = u'название',
        max_length = 200,
    )
    price = models.DecimalField(
        verbose_name = u'цена',
        decimal_places = 2,
        max_digits = 10,
    )
    test_items_quantity = models.IntegerField(
        verbose_name = u'количество тестов в упаковке'
    )
    # timestamps
    created_at = models.DateTimeField(
        verbose_name = u'дата создания',
        default = datetime.now(),
        editable = False,
    )
    updated_at = models.DateTimeField(
        verbose_name = u'дата изменения',
        auto_now = True,
    )

    class Meta:
        ordering = ['-created_at', '-id',]
        verbose_name = u'товар'
        verbose_name_plural = u'товары'

    def __unicode__(self):
        return self.title


PAYMENT_TYPE_CHOICES = (
        ('cash', 'наличными'),
        ('credit_card', 'кредиткой'),
    )

ORDER_STATE_CHOICES = (
        ('new', 'новый'),
    )

class Order(models.Model):
    product = models.ForeignKey(
        'Product',
        verbose_name = 'тип товара'
    )
    product_quantity = models.IntegerField(
        verbose_name = u'количество',
    )
    initials = models.CharField(
        verbose_name = u'инициалы',
        max_length = 300,
    )
    email = models.CharField(
        verbose_name = u'e-mail',
        max_length = 200,
    )
    allow_mailings = models.BooleanField(
        verbose_name = u'разрешение на рассылку',
    )
    city = models.CharField(
        verbose_name = u'город',
        max_length = 200,
    )
    address = models.TextField(
        verbose_name = u'адрес',
    )
    phone = models.CharField(
        verbose_name = u'номер телефона',
        max_length = 200,
    )
    payment_type = models.CharField(
        verbose_name = u'тип платежа',
        max_length = 200,
        choices = PAYMENT_TYPE_CHOICES,
    )
    # пояснение для оплаты наличными
    cash_pay_sum = models.CharField(
        verbose_name = u'сумма наличных для оплаты',
        max_length = 100,
        help_text = 'с какой суммы готовить сдачу',
    )
    state = models.CharField(
        verbose_name = u'статус заказа',
        max_length = 200,
        choices = ORDER_STATE_CHOICES,
        default = 'new',
    )
    # timestamps
    created_at = models.DateTimeField(
        verbose_name = u'дата создания',
        default = datetime.now(),
        editable = False,
    )
    updated_at = models.DateTimeField(
        verbose_name = u'дата изменения',
        auto_now = True,
    )

    def total(self):
        return self.product.price*self.product_quantity

    class Meta:
        ordering = ['-created_at', '-id',]
        verbose_name = u'заказ'
        verbose_name_plural = u'заказы'

    def __unicode__(self):
        return self.product.title + self.initials

