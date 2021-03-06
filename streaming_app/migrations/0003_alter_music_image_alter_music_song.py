# Generated by Django 4.0.5 on 2022-06-09 17:31

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('streaming_app', '0002_alter_music_image_alter_music_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='image',
            field=models.FileField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='images'),
        ),
        migrations.AlterField(
            model_name='music',
            name='song',
            field=models.FileField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='songs'),
        ),
    ]
