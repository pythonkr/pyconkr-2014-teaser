from django.contrib import admin
from page.models import SiteConfig


class SiteConfigAdmin(admin.ModelAdmin):
    exclude = []

    def get_form(self, request, obj=None, **kwargs):
        leaves = {1: 'config_boolean', 2: 'config_integer', 3: 'config_varchar', 4: 'config_text', 5: 'config_datetime'}
        self.exclude = leaves.values()
        self.exclude.remove(leaves.get(obj.config_type, None))

        return super(SiteConfigAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(SiteConfig, SiteConfigAdmin)
