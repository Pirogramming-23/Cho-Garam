from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=32)
    release = models.CharField(max_length=32)
    genre = models.CharField(max_length=32)
    score = models.CharField(max_length=32)
    runtime = models.CharField(max_length=32)
    director = models.CharField(max_length=32)
    actor = models.CharField(max_length=32)
    content = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
