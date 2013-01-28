# -*- coding: utf-8 -*-
import os
from datetime import datetime

from django.db import models

from sorl.thumbnail import ImageField as sorl_ImageField
from pytils.translit import translify

class ImageField(sorl_ImageField, models.ImageField):
    pass

def file_path_reviews(instance, filename):
    return os.path.join('images','reviews', translify(filename).replace(' ', '_') )

REVIEWER_TYPE_CHOICES = (
    ('doctor', u'Врач'),
    ('patient', u'Пациент'),
)

class Review(models.Model):
    reviewer_type = models.CharField(
        verbose_name = u'тип автора обзора',
        max_length = 30,
        choices = REVIEWER_TYPE_CHOICES
    )
    reviewer_post = models.CharField(
        verbose_name = u'должность',
        max_length = 200,
        blank = True,
        null = True
    )
    initials = models.CharField(
        verbose_name = u'ФИО',
        max_length = 200
    )
    email = models.CharField(
        verbose_name = u'e-mail',
        max_length = 200,
    )
    phone_code = models.CharField(
        verbose_name = u'код телефона',
        max_length = 100,
        blank = True,
        )
    phone = models.CharField(
        verbose_name = u'номер телефона',
        max_length = 200,
        blank = True,
    )
    review = models.TextField(
        verbose_name = u'обзор'
    )  
    image = ImageField(
        verbose_name = u'изображение',
        upload_to = file_path_reviews,
        blank = True
    )
    is_published = models.BooleanField(
        verbose_name = u'признак публикации'
    )

    # timestamps
    created_at = models.DateTimeField(
        verbose_name = u'дата создания',
        default = datetime.now(),
        editable = False
    )
    updated_at = models.DateTimeField(
        verbose_name = u'дата изменения',
        auto_now = True,
        default = datetime.now(),
    )

    def __unicode__(self):
        return self.initials

    class Meta:
        ordering = ['-created_at', '-id',]
        verbose_name = u'отзыв'
        verbose_name_plural = u'отзывы'