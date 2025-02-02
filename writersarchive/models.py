from django.db import models
from django.contrib.auth.models import User

POSTSTATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Story(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    content = models.TextField()
    dateposted = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=POSTSTATUS, default=0)