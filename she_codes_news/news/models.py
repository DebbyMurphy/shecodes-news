from django.contrib.auth import get_user_model
from django.db import models


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_url = models.URLField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

class Author(models.Model):
    pass
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     title = models.CharField(max_length=100)
#     content = models.TextField(max_length=1000)

