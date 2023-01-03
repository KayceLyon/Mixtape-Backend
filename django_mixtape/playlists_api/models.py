from django.db import models

# Create your models here.

class Playlist(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    summary = models.TextField()
    



