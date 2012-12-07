# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Publication, NewsCategory, News, Article

admin.site.register(Publication,)
admin.site.register(NewsCategory,)
admin.site.register(News,)
admin.site.register(Article,)