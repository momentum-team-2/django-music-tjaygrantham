# Generated by Django 3.0.7 on 2020-06-29 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0011_album_artworkurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artworkURL',
            field=models.URLField(max_length=255),
        ),
    ]
