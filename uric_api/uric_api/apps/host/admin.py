from django.contrib import admin

from uric_api.apps.host.models import Host, HostCategory, PkeyModel

# Register your models here.

admin.site.register(Host)
admin.site.register(HostCategory)
admin.site.register(PkeyModel)
