from django.conf.urls import patterns, url
from news.views import NewsListView, NewsDetailView, NewsCreateView

urlpatterns = patterns(
    '',
    url(r'^$', NewsListView.as_view(), name='news_list'),
    url(r'^(?P<pk>\d+)/$', NewsDetailView.as_view(), name='news_detail'),
    url(r'^create/$', NewsCreateView.as_view(), name='news_create'),
)