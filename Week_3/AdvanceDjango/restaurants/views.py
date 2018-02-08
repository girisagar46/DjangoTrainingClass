from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView

from restaurants.models import RestaurantLocation


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['dummy_text'] = "Dummy Text"
        return context


class RestaurantLocationListView(ListView):
    def get_context_data(self, **kwargs):
        context = super(RestaurantLocationListView, self).get_context_data(**kwargs)
        qs = self.get_queryset()
        context['object_list'] = qs
        context['count'] = qs.count()
        return context

    def get_queryset(self):
        queryset = RestaurantLocation.objects.all()
        return queryset






"""
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset
"""