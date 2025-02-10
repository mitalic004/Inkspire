from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

POSTSTATUS = ((0, "Draft"), (1, "Published"))
RATING = ((0, "Not Rated"), (1, "★"), (2, "★★"), (3, "★★★"), (4, "★★★★"), (5, "★★★★★"))
GENRE = ((0, "Action & Adventure"), (1, "Comedy"), (2, "Contemporary"), (3, "Fantasy"), (4, "Historical"), (5, "Horror"), (6, "Mystery"), (7, "Romance"), (8, "Science Fiction"))

# Story Model
class Story(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stories")
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    summary = models.TextField(max_length=500)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    genre = models.IntegerField(choices=GENRE, default=2)
    cover_img = CloudinaryField()
    status = models.IntegerField(choices=POSTSTATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def save(self, *args, **kwargs):
        # Automatically set slug
        if not self.slug:
            self.slug = slugify(self.title)

        # Set cover image based on genre
        if not self.cover_img:
            checkgenre = GenreCoverImage.objects.get(genre_list=self.genre)
            self.cover_img = checkgenre.cover_img

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} | written by {self.author}"

# Comment Model
class Comment(models.Model):
    post = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    rating = models.IntegerField(choices=RATING, default=0)
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"

# Genre Cover Image Model
class GenreCoverImage(models.Model):
    genre_list = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="genres")
    cover_img = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ["genre_list"]