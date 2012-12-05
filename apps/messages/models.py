# coding: utf-8
from datetime import datetime

from django.db import models

from apps.products.models import Product

class MailingAddress(models.Model):
    email = models.CharField(
        verbose_name = 'e-mail',
        max_length = 300,
    )
    is_active = models.BooleanField(
        verbose_name = 'активен',
        default = True,
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
        verbose_name = u'адрес рассылки'
        verbose_name_plural = u'адреса рассылок'

    def __unicode__(self):
        return self.email

PAYMENT_TYPE_CHOICES = (
        ('cash', 'наличными'),
        ('credit_card', 'кредиткой'),
    )

MESSAGE_STATE_CHOICES = (
        ('new', 'новый'),
    )

class Order(models.Model):
    product = models.ForeignKey(
        'products.Product',
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
        verbose_name = u'статус обращения',
        max_length = 200,
        choices = MESSAGE_STATE_CHOICES,
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

    def save(self, *args, **kwargs):
        super(Order, self).save()
        if self.created_at == None:
            if self.allow_mailings:
                self.create_mailing_address()

    def create_mailing_address(self):
        MailingAddress.objects.create(email=self.email, is_active=True)

    def total(self):
        return self.product.price*self.product_quantity

    class Meta:
        ordering = ['-created_at', '-id',]
        verbose_name = u'заказ'
        verbose_name_plural = u'заказы'

    def __unicode__(self):
        return self.product.title + self.initials
