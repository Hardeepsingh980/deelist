from django.db import models
from django.contrib.auth.models import User

class MusicLibrary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    playlists = models.ManyToManyField('Playlist', blank=True)


    def __str__(self):
        return self.user.username


class Playlist(models.Model):
    name = models.CharField(max_length=50)
    songs = models.ManyToManyField('Song', blank=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=50)
    file_name = models.CharField(max_length=100, null=True, blank=True)
    music_url = models.URLField()

    def __str__(self):
        return self.name