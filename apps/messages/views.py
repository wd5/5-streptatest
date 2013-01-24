# coding: utf-8
import re

from django.views.generic import FormView, TemplateView
from django import forms
from django.forms.formsets import formset_factory
from django.http import HttpResponse
from django.template import RequestContext
from django.forms.widgets import RadioSelect
from django.shortcuts import redirect, render_to_response
from captcha.fields import CaptchaField

from apps.publications.models import Article
from apps.products.models import Product
from apps.places.models import City, Drugstore
from apps.messages.models import Question, EntryInSchool
from apps.siteblocks.models import Settings
from models import Order, PartnershipOffer

class OrderForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Order
        exclude = ('state',)
        widgets = {
            'product': RadioSelect(), 
        }

    def clean(self):
        cleaned_data = super(OrderForm, self).clean()
        try:
            email = cleaned_data['email']
            if not re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email):
                self._errors["email"] = self.error_class(['Неправильный формат электронной почты'])
        except:
            self._errors["email"] = self.error_class(['Обязательное поле'])
        return cleaned_data

class OrderFormView(FormView):
    template_name = 'order.html'
    success_url = '/thanks_for_order/'
    form_class = OrderForm

    def get_params(self, request, **kwargs):
        params = request.GET
        return params

    def get_context_data(self, **kwargs):
        context = super(OrderFormView, self).get_context_data(**kwargs)
        params = self.get_params(self.request)
        try:
            context['chosed_product'] = params['chosed_product']
        except:
            context['chosed_product'] = None

        try:
            current_quantity = self.get_form_kwargs()['data']['product_quantity']      
        except:
            current_quantity = 1

        context['drugtest'] = City.objects.all()[0].drugstore_set
        context['drugstore_count'] = Drugstore.objects.all().count
        product_with_5_tests = Product.objects.filter(test_items_quantity=5)[0]
        product_with_20_tests = Product.objects.filter(test_items_quantity=20)[0]
        context['product_with_5_tests'] = product_with_5_tests
        context['product_with_20_tests'] = product_with_20_tests
        context['current_total_5'] = product_with_5_tests.price*int(current_quantity)
        context['current_total_20'] = product_with_20_tests.price*int(current_quantity)
        return context

    def form_valid(self, form):
        data = {key:value for key, value in form.cleaned_data.items() if key is not 'captcha'}
        Order.objects.create(**data)
        return redirect(self.get_success_url())

class PartnersFormDoctors(forms.ModelForm):
    captcha = CaptchaField()
    
    class Meta:
        model = PartnershipOffer
        exclude = ('state',)

    def clean(self):
        cleaned_data = super(PartnersFormDoctors, self).clean()
        try:
            email = cleaned_data['email']
            if not re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email):
                self._errors["email"] = self.error_class(['Неправильный формат электронной почты'])
        except:
            self._errors["email"] = self.error_class(['Обязательное поле'])
        return cleaned_data


class PartnersFormDrugstores(forms.ModelForm):
    captcha = CaptchaField()
    
    class Meta:
        model = PartnershipOffer
        exclude = ('state',)

    def clean(self):
        cleaned_data = super(PartnersFormDrugstores, self).clean()
        try:
            email = cleaned_data['email']
            if not re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email):
                self._errors["email"] = self.error_class(['Неправильный формат электронной почты'])
        except:
            self._errors["email"] = self.error_class(['Обязательное поле'])
        return cleaned_data

class PartnersView(TemplateView):
    template_name = 'partners.html'

    def get_context_data(self, **kwargs):
        context = super(PartnersView, self).get_context_data(**kwargs)
        context['form_doctors'] = PartnersFormDoctors(initial={'offer_author_type': 'doctor'})
        context['form_drugstores'] = PartnersFormDrugstores(initial={'offer_author_type': 'drugstore'})
        context['drugstore_count'] = Drugstore.objects.all().count()
        context['partnership_offer_doctor_text'] = Settings.objects.get(name='partnership_offer_doctor_text').value
        context['partnership_offer_drugstore_text'] = Settings.objects.get(name='partnership_offer_drugstore_text').value
        return context

class PartnersDoctorsFormView(FormView):
    template_name = 'partners.html'
    success_url = '/thanks_partners_doctors/'
    form_class = PartnersFormDoctors

    def get_context_data(self, **kwargs):
        context = super(PartnersDoctorsFormView, self).get_context_data(**kwargs)
        context['drugstore_count'] = Drugstore.objects.all().count()
        context['partnership_offer_doctor_text'] = Settings.objects.get(name='partnership_offer_doctor_text').value
        context['partnership_offer_drugstore_text'] = Settings.objects.get(name='partnership_offer_drugstore_text').value 
        return context

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form_doctors=form))

    def form_valid(self, form):
        data = {key:value for key, value in form.cleaned_data.items() if key is not 'captcha'}
        PartnershipOffer.objects.create(**data)
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form_doctors=form))

class PartnersDrugstoresFormView(FormView):
    template_name = 'partners.html'
    success_url = '/thanks_partners_drugstores/'
    form_class = PartnersFormDrugstores

    def get_context_data(self, **kwargs):
        context = super(PartnersDrugstoresFormView, self).get_context_data(**kwargs)
        context['drugstore_count'] = Drugstore.objects.all().count()
        context['partnership_offer_doctor_text'] = Settings.objects.get(name='partnership_offer_doctor_text').value
        context['partnership_offer_drugstore_text'] = Settings.objects.get(name='partnership_offer_drugstore_text').value 
        return context

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form_drugstores=form))

    def form_valid(self, form):
        data = {key:value for key, value in form.cleaned_data.items() if key is not 'captcha'}
        PartnershipOffer.objects.create(**data)
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form_drugstores=form))


class PatientsView(TemplateView):
    template_name = 'patients.html'

    def get_context_data(self, **kwargs):
        context = super(PatientsView, self).get_context_data(**kwargs)
        context['q_form'] = PatientQForm()
        context['school_form'] = PatientsSchoolForm()
        context['last_articles'] = Article.objects.all()[:2]
        context['articles_more_count'] = Article.objects.all().count()-2
        return context

class PatientQForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Question
        exclude = ('state','answer','send_answer')

    def clean(self):
        cleaned_data = super(PatientQForm, self).clean()
        try:
            email = cleaned_data['email']
            if not re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email):
                self._errors["email"] = self.error_class(['Неправильный формат электронной почты'])
        except:
            self._errors["email"] = self.error_class(['Обязательное поле'])
        return cleaned_data

class PatientsQFormView(FormView):
    form_class = PatientQForm
    template_name = '_new_patients_q_form.html'

    def form_valid(self, form):
        data = {key:value for key, value in form.cleaned_data.items() if key is not 'captcha'}
        Question.objects.create(**data)
        response = 'success!'
        return HttpResponse(response)

    def form_invalid(self, form):
        response = render_to_response(self.template_name, 
                                      self.get_context_data(q_form=form),
                                      context_instance=RequestContext(self.request))
        return HttpResponse(response, status=406)   


class PatientsSchoolForm(forms.ModelForm):
    captcha = CaptchaField() 

    class Meta:
        model = EntryInSchool
        exclude = ('state',)

    def clean(self):
        cleaned_data = super(PatientsSchoolForm, self).clean()
        try:
            email = cleaned_data['email']
            if not re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email):
                self._errors["email"] = self.error_class(['Неправильный формат электронной почты'])
        except:
            self._errors["email"] = self.error_class(['Обязательное поле'])
        return cleaned_data

class PatientsSchoolFormView(FormView):
    form_class = PatientsSchoolForm
    template_name = '_new_patients_school_form.html'

    def form_valid(self, form):
        data = {key:value for key, value in form.cleaned_data.items() if key is not 'captcha'}
        EntryInSchool.objects.create(**data)
        response = 'success!'
        return HttpResponse(response)

    def form_invalid(self, form):
        response = render_to_response(self.template_name, 
                                      self.get_context_data(school_form=form),
                                      context_instance=RequestContext(self.request))
        return HttpResponse(response, status=406)        