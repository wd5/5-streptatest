# -*- coding: utf-8 -*-
from django.views.generic import TemplateView

from apps.reviews.models import Review

class BaseReviewView(TemplateView):
    def get_params(self, request, **kwargs):
        params = request.GET
        return params

class ReviewIndexView(BaseReviewView):
    template_name = 'review_index.html'

    def get_context_data(self, **kwargs):
        context = super(ReviewIndexView, self).get_context_data(**kwargs)
        context['review_list'] = Review.objects.filter(is_published=True)
        return context

class ReviewListView(BaseReviewView):
    template_name = 'review_list.html'

    def get_context_data(self, **kwargs):
        context = super(ReviewListView, self).get_context_data(**kwargs)
        object_list = Review.objects.filter(is_published=True)
        context['object_list'] = object_list.filter(reviewer_type=kwargs['reviewer_type'])[:2]
        return context

class MoreReviewsView(BaseReviewView):
    template_name = '_review_items.html'

    def get_context_data(self, **kwargs):
        context = super(MoreReviewsView, self).get_context_data(**kwargs)
        params = self.get_params(self.request)
        start = int(params['current_items'])
        limit = start+2
        object_list = Review.objects.filter(is_published=True)
        context['object_list'] = object_list.filter(reviewer_type=kwargs['reviewer_type'])[start:limit]
        return context
