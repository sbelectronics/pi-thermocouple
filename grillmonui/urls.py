from django.conf.urls import patterns, url

from grillmonui import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^getTemp$', views.getTemp, name='getTemp'),
)
