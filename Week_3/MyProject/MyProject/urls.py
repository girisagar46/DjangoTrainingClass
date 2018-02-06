from django.conf.urls import url
from django.contrib import admin

from myapp.views import ProductListView

urlpatterns = [
    url(r'^$', ProductListView.as_view()),
    url(r'^admin/', admin.site.urls),
]
