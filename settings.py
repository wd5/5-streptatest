# -*- coding: utf-8 -*-
DATABASE_NAME = u'streptatest'
PROJECT_NAME = u'streptatest'
SITE_NAME = u'Стрептатест'
DEFAULT_FROM_EMAIL = u'support@XXXXXXXXXXX'

from config.base import *

try:
    from config.development import *
except ImportError:
    from config.production import *

TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS += (
    'apps.siteblocks',
    # 'apps.pages',
    # 'apps.faq',
    'apps.slider',
    # 'apps.newsboard',
    # 'apps.orders',
    'apps.inheritanceUser',
    'apps.capabilities',
    'apps.reviews',
    'apps.publications',
    'apps.messages',
    'apps.places',
    'sorl.thumbnail',
    #'captcha',
)

MIDDLEWARE_CLASSES += (
    'apps.pages.middleware.PageFallbackMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'apps.auth_backends.CustomUserModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    # 'apps.pages.context_processors.meta',
    'apps.siteblocks.context_processors.settings',
    'apps.utils.context_processors.authorization_form',
)