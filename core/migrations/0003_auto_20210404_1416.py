# Generated by Django 3.1 on 2021-04-04 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_song_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musiclibrary',
            name='playlists',
            field=models.ManyToManyField(blank=True, to='core.Playlist'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(blank=True, to='core.Song'),
        ),
    ]