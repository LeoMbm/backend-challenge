from django.contrib import admin

from logs.models import Logs, Countries

# Register your models here.
admin.site.register(Logs)
admin.site.register(Countries)