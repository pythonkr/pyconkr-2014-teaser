from django.shortcuts import render
from django.views.generic.base import View


class VenueView(View):
    template_name = 'venue/venue.html'
    def get(self, request):
        ctx = {}
        return render(request, self.template_name, ctx)
