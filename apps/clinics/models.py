# coding: utf-8
from datetime import datetime

from django.db import models

class City(models.Model):
    title = models.CharField(
        verbose_name = u'город',
        max_length = 100,
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

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created_at', '-id',]
        verbose_name = u'город'
        verbose_name_plural = u'города'


class Clinic(models.Model):
    city = models.ForeignKey(
        'City',
        verbose_name = u'город',
    )
    title = models.CharField(
        verbose_name = u'название',
        max_length = 100,

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

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created_at', '-id',]
        verbose_name = u'клиника'
        verbose_name_plural = u'клиники'
