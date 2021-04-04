from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-playlist/', views.add_playlist, name='add-playlist'),
    path('add-song/<int:id>/', views.add_song, name='add-song'),
]
