from django.views.generic import FormView, TemplateView
from django import forms
from django.forms.formsets import formset_factory
from django.http import HttpResponse
from django.forms.widgets import RadioSelect

from apps.products.models import Product
from django.shortcuts import redirect
from apps.places.models import City, Drugstore
from models import Order, PartnershipOffer

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('state',)
        widgets = {
            'product': RadioSelect(), 
        }

class OrderFormView(FormView):
    template_name = 'order.html'
    success_url = '/thanks/'
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

        context['city_list'] = City.objects.all()
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
        Order.objects.create(**form.cleaned_data)
        return redirect(self.get_success_url())

class OrderThanksView(TemplateView):
    template_name = 'success.html'

# ArticleFormSet = formset_factory(ArticleForm)
#     BookFormSet = formset_factory(BookForm)
#     if request.method == 'POST':
#         article_formset = ArticleFormSet(request.POST, request.FILES, prefix='articles')
#         book_formset = BookFormSet(request.POST, request.FILES, prefix='books')
#         if article_formset.is_valid() and book_formset.is_valid():
#             # do something with the cleaned_data on the formsets.
#             pass
#     else:
#         article_formset = ArticleFormSet(prefix='articles')
#         book_formset = BookFormSet(prefix='books')
#     return render_to_response('manage_articles.html', {
#         'article_formset': article_formset,
#         'book_formset': book_formset,
#     })
class PartnersFormDoctors(forms.ModelForm):
    class Meta:
        model = PartnershipOffer
        exclude = ('state',)

class PartnersFormDrugstores(forms.ModelForm):
    class Meta:
        model = PartnershipOffer
        exclude = ('state',)

class PartnersView(TemplateView):
    template_name = 'partners.html'

    def get_context_data(self, **kwargs):
        context = super(PartnersView, self).get_context_data(**kwargs)
        context['form_doctors'] = PartnersFormDoctors(initial={'offer_author_type': 'doctor'})
        context['form_drugstores'] = PartnersFormDrugstores(initial={'offer_author_type': 'drugstore'})
        return context

class PartnersDoctorsFormView(FormView):
    template_name = 'partners.html'
    success_url = '/thanks/'
    form_class = PartnersFormDoctors

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form_doctors=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form_doctors=form))

class PartnersDrugstoresFormView(FormView):
    template_name = 'partners.html'
    success_url = '/thanks/'
    form_class = PartnersFormDrugstores

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form_drugstores=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form_drugstores=form))


        