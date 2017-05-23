from django.db import models
from django.conf import settings


class SFDeal(models.Model):
    """Model to store Sales Force Deal info."""

    name = models.CharField(max_length=255)
    account = models.CharField(max_length=255, blank=True, null=True)
    probability = models.FloatField(blank=True, null=True)
    project_id = models.CharField(max_length=255, unique=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    staff_owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='staff_owner')
    pod = models.CharField(max_length=255, blank=True, null=True)
    staff_manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='staff_manager')
    status = models.ForeignKey('Status', default=None)
    revenue = models.FloatField(blank=True, null=True)
    contract_hours = models.FloatField(blank=True, null=True)
    last_modified_date = models.DateField(auto_now=True)
