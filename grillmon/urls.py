from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xmas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', RedirectView.as_view(url='/grillmon/', permanent=False), name='index'),

    url(r'^grillmon/', include('grillmonui.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
