# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from page.views import Index, About


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^about/$', About.as_view()),
    url(r'^$', Index.as_view()),
)


# static files (for app)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# media files (for user)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)