from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass                            #this is where I would add more fields, like a profile picture

    def __str__(self):
        return self.username
