from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(max_length=500, default="Biography to come")
    profile_img = models.URLField(max_length=200, default="https://image.flaticon.com/icons/svg/104/104784.svg")

    def __str__(self):
        return self.username