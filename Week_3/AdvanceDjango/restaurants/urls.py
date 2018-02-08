from django.conf.urls import url

from .views import HomeView, RestaurantLocationListView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^restaurants/$', RestaurantLocationListView.as_view(), name='restaurants'),
]