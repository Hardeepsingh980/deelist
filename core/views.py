from django.shortcuts import render, redirect
import pyrebase
from django.core.files.storage import default_storage
from urllib.parse import quote
from .forms import AddPlaylistForm, AddSongForm
from django.contrib import messages
from .models import Playlist


config = {
    'apiKey': "AIzaSyDHUIstEguxT4RwJS3JQ00S-p-9fTUKI1I",
    'authDomain': "deelist-17223.firebaseapp.com",
    'projectId': "deelist-17223",
    'storageBucket': "deelist-17223.appspot.com",
    'messagingSenderId': "421207476246",
    'appId': "1:421207476246:web:7f5629986807d692368d37",
    'measurementId': "G-CMLMWCYEPS",
    'databaseURL': ''
}


firebase = pyrebase.initialize_app(config)
storage = firebase.storage()


# def home(request):
#     if request.method == 'POST':
#         file = request.FILES['file']
#         file_save = default_storage.save(file.name, file)
#         file_on_cloud = storage.child("files/" + file.name).put("media/" + file.name)
#         print(file_on_cloud)
#         print('https://firebasestorage.googleapis.com/v0/b/'+file_on_cloud['bucket'] + '/o/' + quote(file_on_cloud['name'], safe='') + '?alt=media')
#         delete = default_storage.delete(file.name)
#     return render(request, 'core/home.html')


def home(request):
    return render(request, 'core/home.html')



def add_playlist(request):
    if request.method == 'POST':
        form = AddPlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save()
            request.user.musiclibrary.playlists.add(playlist)
            messages.info(request, 'Playlist Added Successfully !!')
            return redirect('home')
        else:
            messages.info(request, 'Fix the error !!')
            return render(request, 'core/add-playlist.html', {'form': form})
    else:
        form = AddPlaylistForm()
        return render(request, 'core/add-playlist.html', {'form': form})


def add_song(request, id):
    playlist = Playlist.objects.get(id=id)
    if request.method == 'POST':
        form = AddSongForm(request.POST)
        if form.is_valid():
            song = form.save()
            playlist.songs.add(song)
            messages.info(request, 'Song Added Successfully !!')
            return redirect('home')
        else:
            messages.info(request, 'Fix the error !!')
            return render(request, 'core/add-song.html', {'form': form, 'playlist':playlist})
    else:
        form = AddSongForm()
        return render(request, 'core/add-song.html', {'form': form, 'playlist': playlist})