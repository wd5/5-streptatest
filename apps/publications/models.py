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
        default = datetime.now(),
    )

    class Meta:
        ordering = ['-created_at', '-id',]
        verbose_name = u'научная публикация'
        verbose_name_plural = u'научные публикации'

    def __unicode__(self):
        return self.title


class NewsCategory(models.Model):
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
        default = datetime.now(),
    )

    class Meta:
        ordering = ['-created_at', '-id']
        verbose_name =  u'категория новостей'
        verbose_name_plural = u'категории новостей'

    def __unicode__(self):
        return self.title


class News(models.Model):
    title = models.CharField(
        verbose_name = u'заголовок',
        max_length = 250,
    )
    category = models.ForeignKey(
        'NewsCategory',
        verbose_name = u'категория',
        null = True,
        blank = True,
    )
    # short_text = models.TextField(
    #     verbose_name = u'короткий текст новости',
    # )
    text = models.TextField(
        verbose_name = u'текст новости',
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
        default = datetime.now(),
    )

    class Meta:
        ordering = ['-created_at', '-id',]
        verbose_name = u'новость'
        verbose_name_plural = u'новости'

    def __unicode__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(
        verbose_name = u'заголовок',
        max_length = 250,
    )
    text = models.TextField(
        verbose_name = u'текст',
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
        default = datetime.now(),
    )

    class Meta:
        ordering = ['-created_at', '-id',]
        verbose_name = u'статья пациентам'
        verbose_name_plural = u'статьи пациентам'

    def __unicode__(self):
        return self.title