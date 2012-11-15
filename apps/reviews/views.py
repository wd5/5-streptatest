# -*- coding: utf-8 -*-
from django.views.generic import TemplateView

from apps.reviews.models import Review

class BaseReviewView(TemplateView):
    def get_params(self, request, **kwargs):
        params = request.GET
        return params

class ReviewListView(BaseReviewView):
    template_name = 'review_list.html'

    def get_context_data(self, **kwargs):
        context = super(ReviewListView, self).get_context_data(**kwargs)
        context['review_list'] = Review.objects.filter(is_published=True)
        return context

