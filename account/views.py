# coding=utf-8
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.forms import AuthenticationForm
from account.forms import SiteUserCreationForm


class SignupFormView(View):
    template_name = 'account/signup.html'
    signup_form = SiteUserCreationForm
    ctx = {
        'signup_form': signup_form
    }

    def get(self, request):
        # TODO : login여부 확인
        return render(request, self.template_name, self.ctx)

    def post(self, request):
        form = self.signup_form(request.POST)

        if form.is_valid():
            form.save()
            data = form.cleaned_data
            user = authenticate(username=data['email'],
                                password=data['password1'])
            login(request, user)
            return redirect('index')  # TODO : use 'next_url'
        else:
            self.ctx['errors'] = form.errors
            return render(request, self.template_name, self.ctx)


class LoginFormView(View):
    template_name = 'account/login.html'
    auth_form = AuthenticationForm
    ctx = {
        'auth_form': auth_form
    }

    def get(self, request):
        # TODO : login여부 확인
        return render(request, self.template_name, self.ctx)

    def post(self, request):
        form = self.auth_form(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        else:
            self.ctx['errors'] = form.errors
            return render(request, self.template_name, self.ctx)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')  # TODO : user 'next_url'w
