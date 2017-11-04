from django.contrib import admin
from .models import EmailUser

# Register your models here.
class EmailUserAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password'),
        }),
        ('Extra Informations',{
            'classes': ('collapse',),
            'fields': (
                'first_name',
                'last_name',
                'last_login',
                'date_joined',)
        }),
        ('Authorizations',{
            'classes': ('collapse',),
            'fields': (
                'is_superuser',
                'is_staff',
                'user_permissions',
                'groups',)
        }),
    )

admin.site.register(EmailUser, EmailUserAdmin)
