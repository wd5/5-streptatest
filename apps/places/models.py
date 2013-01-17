# coding: utf-8
from datetime import datetime

from django.db import models

class City(models.Model):
    title = models.CharField(
        verbose_name = u'город',
        max_length = 100,
    )
    coordinates_center = models.CharField(
        verbose_name = u'центр координат',
        max_length = 300,
    )
    zoom = models.IntegerField(
        verbose_name = u'зум',
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

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['id']
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
    address = models.CharField(
        verbose_name = u'адрес',
        max_length = 400,
    )
    phone_code = models.CharField(
        verbose_name = u'код телефона',
        max_length = 100,
        )
    phone = models.CharField(
        verbose_name = u'телефон',
        max_length = 300,
        blank = True,
    )
    coordinates = models.CharField(
        verbose_name = u'координаты',
        max_length = 300,
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

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created_at', '-id',]
        verbose_name = u'клиника'
        verbose_name_plural = u'клиники'


class Drugstore(models.Model):
    city = models.ForeignKey(
        'City',
        verbose_name = u'город',
    )
    title = models.CharField(
        verbose_name = u'название',
        max_length = 100,
    )
    address = models.CharField(
        verbose_name = u'адрес',
        max_length = 400,
    )
    phone_code = models.CharField(
        verbose_name = u'код телефона',
        max_length = 100,
        )
    phone = models.CharField(
        verbose_name = u'телефон',
        max_length = 300,
        blank = True,
    )
    coordinates = models.CharField(
        verbose_name = u'координаты',
        max_length = 300,
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

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created_at', '-id',]
        verbose_name = u'аптека'
        verbose_name_plural = u'аптеки'


class Lab(models.Model):
    city = models.ForeignKey(
        'City',
        verbose_name = u'город',
    )
    title = models.CharField(
        verbose_name = u'название',
        max_length = 100,
    )
    address = models.CharField(
        verbose_name = u'адрес',
        max_length = 400,
    )
    phone_code = models.CharField(
        verbose_name = u'код телефона',
        max_length = 100,
        )
    phone = models.CharField(
        verbose_name = u'телефон',
        max_length = 300,
        blank = True,
    )
    coordinates = models.CharField(
        verbose_name = u'координаты',
        max_length = 300,
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

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created_at', '-id',]
        verbose_name = u'лаборатория'
        verbose_name_plural = u'лаборатории'
        

class Branch(models.Model):
    city = models.ForeignKey(
        'City',
        verbose_name = u'город',
    )
    title = models.CharField(
        verbose_name = u'название',
        max_length = 100,
    )
    address = models.CharField(
        verbose_name = u'адрес',
        max_length = 400,
    )
    phone_code = models.CharField(
        verbose_name = u'код телефона',
        max_length = 100,
        )
    phone = models.CharField(
        verbose_name = u'телефон',
        max_length = 300,
        blank = True,
    )
    coordinates = models.CharField(
        verbose_name = u'координаты',
        max_length = 300,
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

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created_at', '-id',]
        verbose_name = u'филиал'
        verbose_name_plural = u'филиалы'