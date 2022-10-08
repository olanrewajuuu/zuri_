from django.shortcuts import render
from rest_framework import generics

from musicapp.models import Song
from musicapp.serializers import SongSerializer

# Create your views here.
class list_create_song(generics.ListCreateAPIView):

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

list_create_song_view = list_create_song.as_view()