# coding=utf-8
from account.models import SiteUser
from django import forms
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm


class SiteUserCreationForm(forms.ModelForm):
    class Meta:
        model = SiteUser
        fields = ['email', 'name']

    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput
    )

    def save(self, commit=True):
        user = super(SiteUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
