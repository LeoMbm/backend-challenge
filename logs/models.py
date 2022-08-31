from django.contrib.gis.geoip2.resources import Country
from django.db import models

from IPview import settings


# Create your models here.
class Logs(models.Model):
    ip = models.CharField(max_length=255, null=False, blank=True)
    country = models.CharField(max_length=255, default='Anonymous User', null=False, blank=True)
    date = models.CharField(max_length=255, null=False, blank=True)

    def __int__(self):
        return self.ip


class Countries(models.Model):
    country = models.CharField(max_length=255, null=True, blank=True)
    ip_id = models.ForeignKey(Logs, on_delete=models.CASCADE)

    def __int__(self):
        return self.country
