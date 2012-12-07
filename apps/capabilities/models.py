# -*- coding: utf-8 -*-
import os
from datetime import datetime

from django.db import models

from sorl.thumbnail import ImageField as sorl_ImageField
from pytils.translit import translify

class ImageField(sorl_ImageField, models.ImageField):
    pass

def file_path_capabilities(instance, filename):
    return os.path.join('images','capabilities', translify(filename).replace(' ', '_') )


class Capability(models.Model):
    title = models.CharField(
        verbose_name = u'заголовок',
        max_length = 100
    )
    body = models.TextField(
        verbose_name = u'Описание'
    )
    show_on_index = models.BooleanField(
        verbose_name = u'показывать на главной',
    )
    image = ImageField(
        verbose_name = u'изображение',
        upload_to = file_path_capabilities,
        blank = True
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

    class Meta:
        ordering = ['-created_at', '-id',]
        verbose_name = u'возможность'
        verbose_name_plural = u'возможности'

    def __unicode__(self):
        return self.title

