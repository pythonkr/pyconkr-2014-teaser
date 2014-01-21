from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from pyconkr import views

urlpatterns = patterns('',
    url(r'^$', views.pages.Index.as_view()),

    url(r'^admin/', include(admin.site.urls)),
)
