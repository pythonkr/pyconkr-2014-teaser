from django.conf import settings
from django.views.generic import TemplateView

from pyconkr.models import Program, Sponsor, Speaker


class Home(TemplateView):
    template_name = 'page/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['programs'] = Program.objects.all()
        context['sponsors'] = Sponsor.objects.all()
        context['speakers'] = Speaker.objects.all()
        context['CACHE_TIMEOUT'] = settings.TEMPLATE_CACHE_TIMEOUT
        return context
