from django.conf.urls import patterns, url
from views import AddMessage


urlpatterns = patterns('',
    url('^contact/$', AddMessage.as_view(), name='add-message'),
)