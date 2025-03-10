from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from datetime import datetime

from .models import Product, Purchase

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)


class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['product', 'person', 'address']

    def form_valid(self, form):
        self.object = form.save()
        info = ''
        if (self.object.date == datetime.now()):
            info = 'В честь вашего дня рождения, вам будет предоставлена скидка 10%!'
        return HttpResponse(f'Спасибо за покупку, {self.object.person}! {info}')

