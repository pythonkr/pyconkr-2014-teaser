from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'page/index.html'


class About(TemplateView):
    template_name = 'page/about.html'

