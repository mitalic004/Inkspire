from django.db import models
from django.contrib.auth.models import User

GENRE = ((0, "Action & Adventure"), (1, "Comedy"), (2, "Contemporary"), (3, "Fantasy"), (4, "Historical"), (5, "Horror"), (6, "Mystery"), (7, "Romance"), (8, "Science Fiction"))

# Create your models here.
# Story Submission Model
class Submission(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="submissionauthor")
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    summary = models.TextField(max_length=500)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    genre = models.IntegerField(choices=GENRE, default=2)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Story submission from {self.author}"