from django.shortcuts import render
from rest_framework import generics
from .serializers import PlaylistSerializer
from .models import Playlist


# Create your views here.

class PlaylistList (generics.ListCreateAPIView):
    queryset = Playlist.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = PlaylistSerializer # tell django what serializer to use

class PlaylistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all().order_by('id')
    serializer_class = PlaylistSerializer