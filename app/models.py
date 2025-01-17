from django.contrib.auth.models import AbstractUser
from django.db import models


class AppUser(AbstractUser):
    job = models.CharField(max_length=100, blank=True)
