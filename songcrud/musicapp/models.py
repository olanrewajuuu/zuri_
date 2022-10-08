from django.db import models

# Create your models here.

class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.ImageField


class Song(models.Model):
    title = models.CharField(max_length=50)
    date_released = models.DateField(blank=True)
    likes = models.IntegerField(blank=True)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE)


class Lyric(models.Model):
    content = models.TextField()
    song = models.OneToOneField(Song,on_delete=models.CASCADE,primary_key=True)