# -*- coding: utf-8 -*-
from django.views.generic import TemplateView

from apps.capabilities.models import Capability
from apps.siteblocks.models import Settings

class CapabilityListView(TemplateView):
    template_name = 'capability_list.html'

    def get_context_data(self, **kwargs):
        context = super(CapabilityListView, self).get_context_data(**kwargs)
        context['capability_list'] = Capability.objects.filter(show_on_index=False)
        context['center_text'] = Settings.objects.get(name='capabilities_center_text').value
        context['capabilities_doctor_text_1'] = Settings.objects.get(name='capabilities_doctor_text_1').value
        context['capabilities_doctor_text_2'] = Settings.objects.get(name='capabilities_doctor_text_2').value
        context['capabilities_lab_text_1'] = Settings.objects.get(name='capabilities_lab_text_1').value
        context['capabilities_lab_text_2'] = Settings.objects.get(name='capabilities_lab_text_2').value
        return context
