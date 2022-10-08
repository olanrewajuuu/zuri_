from django.db import models

# Create your models here.

class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.ImageField


class Song(models.Model):
    title = models.CharField(max_length=50)
    date_released = models.DateField
    likes = models.ImageField
    artiste_id = models.ForeignKey(Artist,on_delete=models.CASCADE)


class Lyric(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song,on_delete=models.CASCADE)