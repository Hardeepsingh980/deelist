from django.contrib import admin
from .models import *

admin.site.register(MusicLibrary)
admin.site.register(Playlist)
admin.site.register(Song)