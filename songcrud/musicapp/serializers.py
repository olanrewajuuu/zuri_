from rest_framework import serializers

from musicapp.models import Artist, Lyric, Song


class LyricSerializer(serializers.Serializer):

    class Meta:
        model = Lyric
        fields = [
            'content'
        ]

class SongSerializer(serializers.ModelSerializer):

    artist = serializers.SlugRelatedField(
        slug_field='first_name',
        queryset=Artist.objects.all(),
        many=False,
    )

    class Meta:
        model = Song
        fields = [
            'title',
            'artist',
            'date_released',
            'likes',
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
