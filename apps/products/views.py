from django.views.generic import FormView
from django import forms
from django.http import HttpResponse

from models import Order, Product

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order

class OrderFormView(FormView):
    template_name = 'order.html'
    form_class = OrderForm

    def form_valid(self, form):
        Order.objects.create(**form.cleaned_data)
        response = 'success!'
        return HttpResponse(response)