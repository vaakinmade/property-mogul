from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^search$', views.SearchMogulView.as_view(), name='search'),
]