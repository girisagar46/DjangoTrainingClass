from django.conf.urls import url, include
from django.views.generic import TemplateView

from .views import ContactView, PostDetailView, PostListView, search, post_new, contact_us


urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post_view'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^about/', TemplateView.as_view(template_name='blog/about.html'), name='about'),
    # url(r'^contact/', ContactView.as_view(), name='contact'),
    url(r'^contact/', contact_us, name='contact'),
    url(r'^search/', search, name='search'),
    url(r'^new/$', post_new, name='post_new'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]