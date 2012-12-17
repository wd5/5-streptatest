from django.views.generic import FormView, TemplateView
from django import forms
from django.http import HttpResponse
from django.forms.widgets import RadioSelect

from apps.products.models import Product
from django.shortcuts import redirect
from apps.places.models import City, Drugstore
from models import Order

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

        