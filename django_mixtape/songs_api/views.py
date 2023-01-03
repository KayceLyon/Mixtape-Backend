from django.shortcuts import render
from rest_framework import generics
from .serializers import SongSerializer
from .models import Song

# Create your views here.

class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
