from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simplebtm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ipm.views.home', name='home'),
    url(r'^list/$', 'ipm.views.list', name='list'),
    url(r'^search.*$', 'ipm.views.search', name='search'),
    url(r'^found_tags/$', 'ipm.views.found_tags', name='found_tags'),
)
