# coding=utf-8
from django.shortcuts import render
from django.views.generic.base import View
from .models import Sponsor


class SponsorListView(View):
    template_name = 'sponsor/list.html'

    def get(self, request):
        sponsors = Sponsor.objects.all()

        ctx = {
            'sponsors': sponsors
        }
        return render(request, self.template_name, ctx)
