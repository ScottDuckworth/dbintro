import django
if django.VERSION[:2] <= (1, 3):
  from django.conf.urls.defaults import patterns, include, url
else:
  from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dbintro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^messages/', include('messageboard.urls')),
)
