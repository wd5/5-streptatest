from django.views.generic import FormView
from django.forms import ModelForm

from models import Order, Product

class OrderForm(ModelForm):
    class Meta:
        model = Order

class OrderFormView(FormView):
    template_name = 'order.html'
    form_class = OrderForm