# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.views.generic.base import TemplateResponseMixin

from apps.reviews.models import Review

class BaseIndexView(TemplateView):
    def get_params(self, request, **kwargs):
        params = request.GET
        return params

class LastReviewsMixin(TemplateResponseMixin):
    def get_context_data(self, **kwargs):
        context = super(LastReviewsMixin, self).get_context_data(**kwargs)
        review_list = Review.objects.filter(is_published=True)
        context['doctors_last_review_list'] = review_list.filter(reviewer_type='doctor')[:3]
        context['patients_last_review_list'] = review_list.filter(reviewer_type='patient')[:3]
        return context

class IndexView(LastReviewsMixin, BaseIndexView):
    template_name = 'index.html'

index = IndexView.as_view()