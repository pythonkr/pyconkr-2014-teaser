from django.conf import settings
from django.views.generic import TemplateView

from pyconkr.models import (Program, Sponsor, Speaker,
                            SiteConfiguration, Room, Track)

class Coc(TemplateView):
    template_name = 'page/coc.html'

    def get_context_data(self, **kwargs):
        context = super(Coc, self).get_context_data(**kwargs)
        return context
 

class Home(TemplateView):
    template_name = 'page/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        #context['programs'] = Program.objects.all().order_by('start')
        context['rooms'] = Room.objects.all()
        context['tracks'] = Track.objects.all()
        context['sponsors'] = Sponsor.objects.all()
        context['speakers'] = Speaker.objects.all()
        context['CACHE_TIMEOUT'] = settings.TEMPLATE_CACHE_TIMEOUT
        config = SiteConfiguration.objects.get()
        context['is_proposal_now'] = config.proposal_now
        context['registration_url'] = config.registration_url
        return context
