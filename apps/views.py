# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.views.generic.base import TemplateResponseMixin

from apps.reviews.models import Review
from apps.capabilities.models import Capability
from apps.siteblocks.models import Settings

class IndexSettings(TemplateResponseMixin):
    def get_context_data(self, **kwargs):
        context = super(IndexSettings, self).get_context_data(**kwargs)
        context['header_right_text_1'] = Settings.objects.get(name='index_header_right_text_1').value
        context['header_right_text_2'] = Settings.objects.get(name='index_header_right_text_2').value
        context['header_center_text'] = Settings.objects.get(name='index_header_center_text').value
        return context

class LastReviews(TemplateResponseMixin):
    def get_context_data(self, **kwargs):
        context = super(LastReviews, self).get_context_data(**kwargs)
        review_list = Review.objects.filter(is_published=True)
        context['doctors_last_review_list'] = review_list.filter(reviewer_type='doctor')[:3]
        context['patients_last_review_list'] = review_list.filter(reviewer_type='patient')[:3]
        return context

class IndexCapabilityList(TemplateResponseMixin):
    def get_context_data(self, **kwargs):
        context = super(IndexCapabilityList, self).get_context_data(**kwargs)
        context['index_capability_list'] = Capability.objects.filter(show_on_index=True)
        return context

class IndexView(IndexSettings, LastReviews, IndexCapabilityList, TemplateView):
    template_name = 'index.html'

index = IndexView.as_view()

class InstructionsView(TemplateView):
    template_name = 'pages/instructions.html'

    def get_context_data(self, **kwargs):
        context = super(InstructionsView, self).get_context_data(**kwargs)
        context['instructions_video'] = Settings.objects.get(name='instructions_video').value
        return context

class PatientsView(TemplateView):
    template_name = 'pages/patients.html'

class PartnersView(TemplateView):
    template_name = 'pages/partners.html'