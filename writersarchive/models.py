from django.db import models
from django.contrib.auth.models import User

POSTSTATUS = ((0, "Draft"), (1, "Published"))
RATING = ((0, "Not Rated"), (1, "★"), (2, "★★"), (3, "★★★"), (4, "★★★★"), (5, "★★★★★"))

# Create your models here.
class Story(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stories")
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    summary = models.TextField(max_length=500)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    posted_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=POSTSTATUS, default=0)


class Comment(models.Model):
    post = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    rating = models.IntegerField(choices=RATING, default=0)
    comment_text = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)