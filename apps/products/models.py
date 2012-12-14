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
        default = datetime.now(),
    )

    class Meta:
        ordering = ['-created_at', '-id',]
        verbose_name = u'товар'
        verbose_name_plural = u'товары'

    def __unicode__(self):
        return self.title

