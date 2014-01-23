# coding=utf-8
from django.shortcuts import render
from django.views.generic.base import View
from .models import News


class NewsListView(View):
    template_name = 'news/list.html'

    def get(self, request):
        posts = News.objects.all()

        ctx = {
            'posts': posts
        }
        return render(request, self.template_name, ctx)


class NewsDetailView(View):
    template_name = 'news/detail.html'

    def get(self, request, post_id):
        post = News.objects.get(id=post_id)

        ctx = {
            'post': post
        }
        return render(request, self.template_name, ctx)
