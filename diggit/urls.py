from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from links.views import LinkListView

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', LinkListView.as_view(), name='home'), # ^$ is beginning and end, respectively; that refers to /

    url(r"^login/$", "django.contrib.auth.views.login", {"template_name": "login.html"}, name="login"),
    url(r"^logout/$", "django.contrib.auth.views.logout_then_login", name="logout"),

    url(r"^accounts/", include("registration.backends.simple.urls")), #take note that I've specified just a beginning here, no end ($). the registration package appends /register.

)
