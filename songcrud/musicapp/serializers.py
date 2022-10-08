from dataclasses import field, fields
from rest_framework import serializers

from musicapp.models import Lyric, Song, Artist


class LyricSerializer(serializers.Serializer):

    class Meta:
        model = Lyric
        fields = [
            'content'
        ]

class SongSerializer(serializers.ModelSerializer):

    lyric = LyricSerializer(many=False)

    class Meta:
        model = Song
        fields = [
            'title',
            'date_released',
            'likes',
            'artist',
            'lyric'
            ]

class ArtistSerializer(serializers.ModelSerializer):
    
    songs = SongSerializer(many=True)

    class Meta:
        model = Artist
        fields = [
            'first_name',
            'last_name',
            'age',
            'songs'
        ]