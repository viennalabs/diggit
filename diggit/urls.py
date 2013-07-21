from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from links.views import LinkListView

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', LinkListView.as_view(), name='home') # ^$ is beginning and end, respectively; that refers to /

)
