from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^search$', views.SearchMogulView.as_view(), name='search'),
    url(r'(?P<pk>\d+)$', views.ListingDetailView.as_view(), name='detail'),
    url(r'^for-rent$', views.PropertyRentView.as_view(), name='rent'),
    url(r'^for-sale$', views.PropertySaleView.as_view(), name='sale'),
]