from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    adres = models.CharField(max_length=250, verbose_name='Адрес')
