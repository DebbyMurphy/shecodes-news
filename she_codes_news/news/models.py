from django.contrib.auth import get_user_model
from django.db import models


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    content = models.TextField()
    image_url = models.URLField(max_length=200, default="https://images.unsplash.com/photo-1552912140-6b3c254f5214?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80")
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE, 
        related_name="published_stories"
    )
