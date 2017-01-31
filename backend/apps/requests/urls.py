from django.conf.urls import patterns, url
from views import AddRequest, PricingList


urlpatterns = patterns('',
    url('^request/$', AddRequest.as_view(), name='add-request'),
    url('^pricing/$', PricingList.as_view(), name='pricing-list'),
)