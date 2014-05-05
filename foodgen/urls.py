from django.conf.urls import patterns, include, url
from .views import WelcomeView, GenList, RandomView, RandomFastFoodView, RandomSitDownView,RandomLessThanView, RandomMoreThanView

# Uncomment the next two lines to enable the admin:


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc.views.home', name='home'),
    # url(r'^gisc/', include('gisc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^welcome$', WelcomeView.as_view(), name = 'welcome'),
    url(r'^food$', GenList.as_view(), name = 'genlist'),
    url(r'^random$', RandomView.as_view(), name = 'random'),
    url(r'^random_fastfood$', RandomFastFoodView.as_view(), name = 'random_fastfood'),
    url(r'^random_sitdown$', RandomSitDownView.as_view(), name = 'random_sitdown'),
    url(r'^random_lessthan10$', RandomLessThanView.as_view(), name = 'random_lessthan10'),
    url(r'^random_morethan10$', RandomMoreThanView.as_view(), name = 'random_morethan10'),


)
