import uuid
from datetime import datetime

from django.db import models
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.
class App_User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, null=False, blank=True)
    username = models.CharField(max_length=30, unique=True, null=False,blank=True)
    password = models.CharField(max_length=255, null=False, blank=True)
    slug = models.SlugField(max_length=30, unique=True)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        value = self.username
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

