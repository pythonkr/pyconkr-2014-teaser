# -*- coding:utf-8 -*-
from django.contrib import admin
from solo.admin import SingletonModelAdmin
from django_summernote.admin import SummernoteModelAdmin

from models import Speaker, Sponsor, Program, SiteConfiguration


class ProgramAdmin(SummernoteModelAdmin):
    list_display = ('id', 'title', 'speaker', 'start', 'description')
    ordering = ('-id',)
    search_fields = ('title', 'speaker__name', 'description')


class SponsorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'logo', 'link',)
    ordering = ('-id',)
    search_fields = ('title', 'link')


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company', 'link')
    ordering = ('-id',)
    search_fields = ('name', 'company', 'link', 'intro')


admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(SiteConfiguration, SingletonModelAdmin)
