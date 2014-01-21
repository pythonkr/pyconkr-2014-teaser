from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

from pyconkr import views

urlpatterns = patterns('',
    url(r'^$', views.pages.Index.as_view()),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),

    url(r'^admin/', include(admin.site.urls)),
)
