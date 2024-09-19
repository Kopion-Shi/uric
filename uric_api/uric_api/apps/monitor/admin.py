from django.contrib import admin

# Register your models here.

from django.contrib import admin
from uric_api.apps.monitor.models import MonitorParams


# Register your models here.

@admin.register(MonitorParams)
class MonitorParamsAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_show', 'orders', 'is_deleted','created_time', 'updated_time', 'description')
    search_fields = list_display
    list_filter = list_display
