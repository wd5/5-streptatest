# -*- coding: utf-8 -*-
from datetime import datetime

from apps.siteblocks.models import Settings
from apps.places.models import City
from settings import SITE_NAME

def settings(request):
    try:
        contacts = Settings.objects.get(name='contacts_block').value
    except Settings.DoesNotExist:
        contacts = False

    now = datetime.now()

    city_list = City.objects.all()

    return {
        'contacts': contacts,
        'site_name': SITE_NAME,
        'now': now,
        'city_list': city_list,
    }