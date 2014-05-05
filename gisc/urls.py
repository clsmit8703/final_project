from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc.views.home', name='home'),
    # url(r'^gisc/', include('gisc.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('foodgen.urls', namespace='foodgen')),
)