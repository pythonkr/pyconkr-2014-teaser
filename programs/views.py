from django.shortcuts import render
from django.views.generic import View


class ProgramsView(View):
    template_name = 'programs/programs.html'

    def get(self, request):
        return render(request, self.template_name, {
        })
