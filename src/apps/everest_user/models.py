# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRoleEnum(object):
    STAFFING_OWNER = 1
    STAFFING_MANAGER = 2
    FINANCIAL_OWNER = 3


ROLE_CHOICES = [
    [UserRoleEnum.STAFFING_OWNER, 'Staffing Owner'],
    [UserRoleEnum.STAFFING_MANAGER, 'Staffing Manager'],
    [UserRoleEnum.FINANCIAL_OWNER, 'Sales Associate'],
]


class User(AbstractUser):
    username = models.EmailField(max_length=255, blank=False, null=False, unique=True,
                                 verbose_name='Email ID')
    role = models.IntegerField(choices=ROLE_CHOICES, blank=False, null=True)
    temporary_password = models.CharField(max_length=120, blank=True, null=True)
    phone_number = models.CharField(max_length=25, blank=True, null=True,)
    needs_password_change = models.BooleanField(default=True, help_text='If selected user will be forced to change'
                                                                        ' their password when they login',
                                                verbose_name='Force password change')
