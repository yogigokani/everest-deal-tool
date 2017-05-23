# -*- coding: utf-8; mode: django -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User


class UserAdmin(UserAdmin):
    fieldsets = (
        ('Account Credentials', {'fields': ('username', 'password', 'needs_password_change')}),
        ('Personal Information', {'fields': (('first_name', 'last_name'), 'phone_number', 'role')}),
        ('Permissions', {'classes': ('collapse',), 'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important Dates', {'classes': ('collapse',), 'fields': ('date_joined', 'last_login')}),
        ('Advanced Options', {'classes': ('collapse',), 'fields': ('temporary_password',)}),
    )

    list_display = ('username', 'full_name', 'phone_number', 'role', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('role', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'first_name', 'last_name')

    def full_name(self, obj):
        return obj.get_full_name()
    full_name.short_description = 'Name'


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
