# coding=utf-8
from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from django.views.generic.base import TemplateView
from .models import News
from news.forms import NewsCreateForm


class NewsListView(TemplateView):
    template_name = 'news/list.html'

    def get_context_data(self, **kwargs):
        ctx = super(NewsListView, self).get_context_data(**kwargs)
        ctx['posts'] = News.objects.all()
        return ctx


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/detail.html'


class NewsCreateView(CreateView):
    model = News
    template_name = 'news/create.html'
    form_class = NewsCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user  # TODO: SiteUser유저로 바꿔야 작동함 김슬님 부탁해요.
        return super(NewsCreateView, self).form_valid(form)
