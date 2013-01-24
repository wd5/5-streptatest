# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView
from django.views.generic.base import TemplateResponseMixin
from django.forms import ModelForm
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import RequestContext

from captcha.fields import CaptchaField

from apps.reviews.models import Review
from apps.capabilities.models import Capability
from apps.siteblocks.models import Settings
from apps.messages.models import MailingAddress


class SubscribeForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = MailingAddress
        exclude = ('is_active',)

    def clean(self):
        cleaned_data = super(SubscribeForm, self).clean()
        try:
            email = cleaned_data['email']
            if not re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email):
                self._errors["email"] = self.error_class(['Неправильный формат электронной почты'])
        except:
            self._errors["email"] = self.error_class(['Обязательное поле'])
        return cleaned_data


class IndexSettings(TemplateResponseMixin):
    def get_context_data(self, **kwargs):
        context = super(IndexSettings, self).get_context_data(**kwargs)
        context['subscribe_form'] = SubscribeForm()
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
        context['instructions_modal_text'] = Settings.objects.get(name='instructions_modal_text').value
        return context

class PatientsView(TemplateView):
    template_name = 'pages/patients.html'


class SubscribeFormView(FormView):
    form_class = SubscribeForm
    template_name = '_new_subscribe_form.html'

    def form_valid(self, form):
        data = {key:value for key, value in form.cleaned_data.items() if key is not 'captcha'}
        MailingAddress.objects.create(**data)
        response = 'success!'
        return HttpResponse(response)

    def form_invalid(self, form):
        response = render_to_response(self.template_name, 
                                      self.get_context_data(subscribe_form=form),
                                      context_instance=RequestContext(self.request))
        return HttpResponse(response, status=406)
