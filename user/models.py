from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users')
    birthdate = models.DateField(default=timezone.now)
    phone = models.CharField(max_length=15)
    adress = models.CharField(max_length=250, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('home')
