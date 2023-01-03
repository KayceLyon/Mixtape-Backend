from rest_framework import serializers
from .models import Playlist

class PlaylistSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Playlist # tell django which model to use
        fields = ('id', 'title', 'author', 'summary',) # tell django which fields to include