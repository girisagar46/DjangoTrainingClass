from django.conf.urls import url

from .views import post_list, PostListView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post_list'),
	#url(r'^$', post_list, name='post_list'),
]