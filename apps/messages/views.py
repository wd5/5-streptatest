from django.views.generic import FormView
from django import forms
from django.http import HttpResponse

from models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('state',)

class OrderFormView(FormView):
    template_name = 'order.html'
    form_class = OrderForm

    def get_context_data(self, **kwargs):
        context = super(OrderFormView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        Order.objects.create(**form.cleaned_data)
        response = 'success!'
        return HttpResponse(response)