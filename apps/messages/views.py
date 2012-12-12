from django.views.generic import FormView
from django import forms
from django.http import HttpResponse
from django.forms.widgets import RadioSelect

from apps.products.models import Product
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
        context['product_with_5_tests'] = Product.objects.filter(test_items_quantity=5)[0]
        context['product_with_20_tests'] = Product.objects.filter(test_items_quantity=20)[0]
        return context

    def form_valid(self, form):
        Order.objects.create(**form.cleaned_data)
        response = 'success!'
        return HttpResponse(response)