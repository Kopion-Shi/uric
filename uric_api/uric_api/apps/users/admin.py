from django.contrib import admin

from uric_api.apps.users.models import User, Menu, Permission


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if obj.password and not obj.password.startswith('pbkdf2_sha256'):
            obj.set_password(obj.password)
        super().save_model(request, obj, form, change)


admin.site.register(User, UserAdmin)
admin.site.register(Menu)
admin.site.register(Permission)
