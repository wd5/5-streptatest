# -*- coding: utf-8 -*-
from datetime import datetime

from apps.siteblocks.models import Settings
from apps.places.models import City
from settings import SITE_NAME
from apps.views import SubscribeForm

def settings(request):
    try:
        contacts = Settings.objects.get(name='contacts_block').value
    except Settings.DoesNotExist:
        contacts = ''

    try:
        like_widget_code = Settings.objects.get(name='like_widget_code').value
    except Settings.DoesNotExist:
        like_widget_code = ''

    try:
        facebook_widget_code = Settings.objects.get(name='facebook_widget_code').value
    except Settings.DoesNotExist:
        pass

    try:
        vk_widget_code = Settings.objects.get(name='vk_widget_code').value
    except Settings.DoesNotExist:
        pass

    try:
        youtube_link = Settings.objects.get(name='youtube_link').value
    except Settings.DoesNotExist:
        pass

    subscribe_form = SubscribeForm()    
    now = datetime.now()

    city_list = City.objects.all()

    return {
        'contacts': contacts,
        'site_name': SITE_NAME,
        'now': now,
        'city_list': city_list,
        'like_widget_code': like_widget_code,
        'facebook_widget_code': facebook_widget_code,
        'subscribe_form': subscribe_form,
        'vk_widget_code': vk_widget_code,
        'youtube_link': youtube_link,  
    }