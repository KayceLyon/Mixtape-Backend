from django.db import models
from playlists_api.models import Playlist

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    cover = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    playlist = models.ForeignKey(Playlist, related_name='songs', null=True, on_delete=models.SET_NULL)