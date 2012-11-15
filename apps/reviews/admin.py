# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from apps.utils.widgets import Redactor
from models import Review

admin.site.register(Review,)