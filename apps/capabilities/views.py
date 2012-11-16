# -*- coding: utf-8 -*-
from django.views.generic import TemplateView

from apps.capabilities.models import Capability
from apps.siteblocks.models import Settings

class CapabilityListView(TemplateView):
    template_name = 'capability_list.html'

    def get_context_data(self, **kwargs):
        context = super(CapabilityListView, self).get_context_data(**kwargs)
        context['capability_list_top'] = Capability.objects.filter(show_in_block='top')
        context['capability_list_bottom'] = Capability.objects.filter(show_in_block='bottom')
        context['top_text'] = Settings.objects.get(name='capabilities_top_text')
        context['center_text'] = Settings.objects.get(name='capabilities_center_text')
        return context
