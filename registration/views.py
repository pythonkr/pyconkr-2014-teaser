from django.shortcuts import render
from django.views.generic import View


class RegistrationView(View):
    template_name = 'registration/registration.html'

    def get(self, request):
        return render(request, self.template_name, {
        })
