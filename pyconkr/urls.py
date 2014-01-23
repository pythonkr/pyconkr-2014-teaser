# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from news.views import NewsListView, NewsDetailView

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
    url(r'^signup/$', SignupFormView.as_view(), name='signup'),
    url(r'^login/$', LoginFormView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    # sponsor
    url(r'^sponsors/$', SponsorListView.as_view(), name='sponsors'),

    # news
    url(r'^news/$', NewsListView.as_view(), name='news_list'),
    url(r'^news/([0-9]+)/$', NewsDetailView.as_view(), name='news_detail'),

    # admin
    url(r'^admin/', include(admin.site.urls)),
)

# static files (for app)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# media files (for user)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
