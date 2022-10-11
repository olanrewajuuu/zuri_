from rest_framework import serializers

from musicapp.models import Artist, Lyrics, Song


class LyricsSerializer(serializers.ModelSerializer):

    song = serializers.PrimaryKeyRelatedField(
        queryset=Song.objects.all(),
        many=False,
        write_only=True
    )

    class Meta:
        model = Lyrics
        fields = [
            'song',
            'content'
        ]


class ArtistSerializer(serializers.ModelSerializer):
    
    songs = serializers.StringRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = Artist
        fields = [
            'first_name',
            'last_name',
            'age',
            'songs',
        ]

class SongSerializer(serializers.ModelSerializer):

    # artist = serializers.PrimaryKeyRelatedField(
    #     queryset=Artist.objects.all(),
    #     many=False,
    # )

    lyrics = LyricsSerializer(read_only=True)

    class Meta:
        model = Song
        fields = [
            'title',
            'artist',
            'date_released',
            'likes',
            'lyrics'
        ]
