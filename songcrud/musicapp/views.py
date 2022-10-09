from rest_framework import generics

from musicapp.models import Artist, Song
from musicapp.serializers import ArtistSerializer, SongSerializer


# Create your views here.

# list or create songs
class list_create_song(generics.ListCreateAPIView):

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

list_create_song_view = list_create_song.as_view()

# get a song
class song_detail(generics.RetrieveAPIView):
    
    queryset = Song.objects.all()
    serializer_class = SongSerializer

song_detail_view = song_detail.as_view()


# list or create artists
class list_create_artist(generics.ListCreateAPIView):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

list_create_artist_view = list_create_artist.as_view()
