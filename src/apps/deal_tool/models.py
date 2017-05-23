from django.db import models
from django.conf import settings
import json


class DealStatusEnum(object):
    PENDING = 1
    PARTIALLY_APPROVED = 2
    APPROVED = 3


DEAL_STATUS_CHOICES = [
    [DealStatusEnum.PENDING, "Pending"],
    [DealStatusEnum.PARTIALLY_APPROVED, "Partially Approved"],
    [DealStatusEnum.APPROVED, "Approved"]
]


class Deal(models.Model):
    """Model to store Sales Force Deal info."""

    name = models.CharField(max_length=255)
    account = models.CharField(max_length=255, blank=True, null=True)
    probability = models.FloatField(blank=True, null=True)
    project_id = models.CharField(max_length=255, unique=True, primary_key=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    staff_owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='staff_owner')
    pod = models.CharField(max_length=255, blank=True, null=True)
    staff_manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='staff_manager')
    status = models.IntegerField(choices=DEAL_STATUS_CHOICES, blank=False, null=False, default=DEAL_STATUS_CHOICES[0][1])
    revenue = models.FloatField(blank=True, null=True)
    contract_hours = models.FloatField(blank=True, null=True)
    last_modified_date = models.DateField(auto_now=True)

    @classmethod
    def list_deals_in_json(cls):
        return json.dumps([str(x) for x in cls.objects.all()])

    def __str__(self):
        return "%s | %s | %s" % (self.project_id, self.account, self.name)
