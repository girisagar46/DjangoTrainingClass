from django.conf.urls import url
from django.views.generic import TemplateView

from .views import ContactView, PostDetailView, PostListView


urlpatterns = [
    # url(r'^$', post_list, name='post_list'),
    url(r'^$', PostListView.as_view(), name='post_view'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^about/', TemplateView.as_view(template_name='blog/about.html'), name='about'),
    url(r'^contact/', ContactView.as_view(), name='contact'),
]