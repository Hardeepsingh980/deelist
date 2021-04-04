from django.forms import ModelForm, Form
from django import forms
from .models import Playlist, Song


class AddPlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        fields = ('name',)


class AddSongForm(ModelForm):
    # music_file = forms.FileField(required=False)
    # music_url = forms.URLField(required=False)

    class Meta:
        model = Song
        fields = ('name', 'music_url')

