from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

                       url('^', include('apps.recipes.urls')),
                       url('^', include('apps.contact.urls')),
                       url('^', include('apps.requests.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       )
