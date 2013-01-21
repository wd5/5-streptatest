# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import RequestContext
from django.utils import simplejson
from django.views.generic import TemplateView, FormView
from django.forms import ModelForm
from captcha.fields import CaptchaField
from django.forms.widgets import RadioSelect

from apps.publications.models import Publication
from apps.places.models import Clinic
from apps.reviews.models import Review
from apps.siteblocks.models import Settings

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in range(0, len(l), n):
        yield l[i:i+n]

class ReviewForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Review
        widgets = {
            'product': RadioSelect(), 
        }

class BaseReviewView(TemplateView):
    def get_params(self, request, **kwargs):
        params = request.GET
        return params

class ReviewIndexView(BaseReviewView):
    template_name = 'review_index.html'

    def get_clinic_list(self, **kwargs):
        all_clinics = Clinic.objects.all()
        latters = []
        for clinic in all_clinics:
            latters.append(clinic.title[0])

        clinic_list = {}
        for latter in latters:
            clinic_list[latter] = []
            for clinic in all_clinics:
                if clinic.title[0] == latter: 
                    clinic_list[latter].append(clinic)
        return clinic_list

    def get_context_data(self, **kwargs):
        context = super(ReviewIndexView, self).get_context_data(**kwargs)
        review_list = Review.objects.filter(is_published=True)
        context['doctors_review_list'] = review_list.filter(reviewer_type='doctor')[:3]
        context['doctors_reviews_count'] = review_list.filter(reviewer_type='doctor').count()-3
        context['patients_review_list'] = review_list.filter(reviewer_type='patient')[:3]
        context['patients_reviews_count'] = review_list.filter(reviewer_type='patient').count()-3
        context['clinic_list'] = self.get_clinic_list()
        context['clinics_count'] = Clinic.objects.all().count()
        context['last_publications'] = Publication.objects.all()[:2]
        context['publications_count'] = Publication.objects.all().count()-2
        context['top_text'] = Settings.objects.get(name='reviews_top_text').value
        return context

class ReviewListView(BaseReviewView):
    template_name = 'review_list.html'

    def get_context_data(self, **kwargs):
        context = super(ReviewListView, self).get_context_data(**kwargs)
        full_object_list = Review.objects.filter(is_published=True).filter(reviewer_type=kwargs['reviewer_type'])
        object_list = full_object_list[:9]
        context['form'] = ReviewForm()
        context['object_list_first'] = object_list[0]
        context['object_list'] = chunks(object_list[1:], 4)
        context['object_list_count'] = full_object_list.filter(reviewer_type=kwargs['reviewer_type']).count
        context['reviewer_type'] = kwargs['reviewer_type']
        return context

class MoreReviewsView(BaseReviewView):
    template_name = '_review_items.html'

    def get_context_data(self, **kwargs):
        context = super(MoreReviewsView, self).get_context_data(**kwargs)
        reviewer_type = kwargs['reviewer_type']
        params = self.get_params(self.request)
        start = int(params['current_items'])
        limit = start+8
        object_list = Review.objects.filter(is_published=True).filter(reviewer_type=reviewer_type)[start:limit]
        context['object_list'] = chunks(object_list, 4)
        context['reviewer_type'] = reviewer_type
        return context

class ReviewFormView(FormView):
    form_class = ReviewForm
    template_name = '_new_review_form.html'

    def get_context_data(self, **kwargs):
        context = super(ReviewFormView, self).get_context_data(**kwargs)
        params = self.request.GET
        try:
            context['reviewer_type'] = params['reviewer_type']
        except:
            pass
        return context

    def form_valid(self, form):
        data = {key:value for key, value in form.cleaned_data.items() if key is not 'captcha'}
        Review.objects.create(**data)
        response = render_to_response('_render_review_form.html', 
                                      self.get_context_data(reviewFormSuccess=1),
                                      context_instance=RequestContext(self.request))
        return HttpResponse(response)

    def form_invalid(self, form):
        response = render_to_response('_render_review_form.html', 
                                      self.get_context_data(form=form, reviewFormSuccess=0),
                                      context_instance=RequestContext(self.request))
        return HttpResponse(response, status=406)
