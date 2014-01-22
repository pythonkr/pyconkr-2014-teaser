from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

from pyconkr import views

urlpatterns = patterns('',
    url(r'^$', views.pages.Index.as_view(), name='index'),
    url(r'^about/$', views.pages.About.as_view()),

    # account
    url(r'^signup/$', views.account.SignupFormView.as_view(), name='signup'),
    url(r'^login/$', views.account.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.account.LogoutView.as_view(), name='logout'),

    url(r'^admin/', include(admin.site.urls)),
)
