<<<<<<< HEAD
from django.utils.translation import gettext as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
=======
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
>>>>>>> 0f02c286ad7fb57f2ec72247fa30dd5bba4155a8

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
<<<<<<< HEAD
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
=======
        (_('Important date'), {'fields': ('last_login',)})
    )
    add_fielsets = (
>>>>>>> 0f02c286ad7fb57f2ec72247fa30dd5bba4155a8
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


<<<<<<< HEAD
admin.site.register(models.User, UserAdmin)
=======
admin.site.register(models.User, UserAdmin)
>>>>>>> 0f02c286ad7fb57f2ec72247fa30dd5bba4155a8
