# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models

class Publication(models.Model):
    title = models.CharField(
        verbose_name = u'заголовок',
        max_length = 250,
    )
    text = models.TextField(
        verbose_name = u'текст',
    )
    where_published = models.CharField(
        verbose_name = u'место публикации',
        max_length = 250,
    )
    link = models.CharField(
        verbose_name = u'ссылка',
        max_length = 200,
    )
    is_published = models.BooleanField(
        verbose_name = u'опубликовано',
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
        verbose_name = u'публикация'
        verbose_name_plural = u'публикации'

    def __unicode__(self):
        return self.title
