from django.conf.urls import url

from ecommerce.views import ProductListView

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='index'),
]