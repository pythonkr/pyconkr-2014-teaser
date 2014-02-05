# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from news.views import NewsListView, NewsDetailView
from programs.views import ProgramsView
from registration.views import RegistrationView
from venue.views import VenueView

admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static
from page.views import Index, About
from account.views import SignupFormView, LoginFormView, LogoutView
from sponsor.views import SponsorListView


urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name='index'),
    url(r'^about/$', About.as_view(), name='about'),

    # account
    url(r'^account/signup/$', SignupFormView.as_view(), name='signup'),
    url(r'^account/login/$', LoginFormView.as_view(), name='login'),
    url(r'^account/logout/$', LogoutView.as_view(), name='logout'),

    url(r'^programs/', ProgramsView.as_view(), name='programs'),
    # registration
    url(r'^registration/', RegistrationView.as_view(), name='registration'),

    # sponsor
    url(r'^sponsors/$', SponsorListView.as_view(), name='sponsors'),

    # news
    url(r'^news/', include('news.urls', app_name='news')),
    
    # venue
    url(r'^venue/$', VenueView.as_view(), name='venue'),

    # admin
    url(r'^admin/', include(admin.site.urls)),
)

# static files (for app)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# media files (for user)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
