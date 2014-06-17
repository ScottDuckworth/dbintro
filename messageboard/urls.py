import django
if django.VERSION[:2] <= (1, 3):
  from django.conf.urls.defaults import patterns, include, url
else:
  from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
  url('^$', views.index),
)
