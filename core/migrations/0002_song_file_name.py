# Generated by Django 3.1 on 2021-04-04 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='file_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
