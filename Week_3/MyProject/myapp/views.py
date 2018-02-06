from django.shortcuts import render
from django.views.generic import ListView

from .models import Product


class ProductListView(ListView):
    #template_name = 'myapp/product_list_backup.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        return context
