from django.db import models

# Create your models here.

class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Song(models.Model):
    title = models.CharField(max_length=50,default='No Title')
    date_released = models.DateField(blank=True)
    likes = models.IntegerField(null=True)

    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name='songs'
    )

    def __str__(self) -> str:
        return f'{self.title}'


class Lyrics(models.Model):
    content = models.TextField(blank=True,editable=True)

    song = models.OneToOneField(
        Song,
        on_delete=models.CASCADE,
        primary_key=True,
    )
