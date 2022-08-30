import uuid
from datetime import datetime

from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.
class App_User(AbstractUser, PermissionsMixin):
    slug = models.SlugField(max_length=30, unique=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        value = self.username
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
