from django.utils import timezone

from django.shortcuts import render
from django.views.generic import ListView

from .models import Product


# def index(request):
#     products = Product.objects.all()
#     ctx = {
#         "products": products
#     }
#     return render(request, 'index.html', context=ctx)


class ProductListView(ListView):
        model = Product

        def get_context_data(self, **kwargs):
            context = super(ProductListView, self).get_context_data(**kwargs)
            context['now'] = timezone.now()
            print(context)
            return context
