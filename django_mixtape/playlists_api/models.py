from django.db import models

# Create your models here.

class Playlist(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    summary = models.TextField()
    
class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    cover = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)




# title
# author username
# summary
# songs will be linked thru playlist id
