# Generated by Django 3.0.7 on 2020-06-28 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0004_album_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='name',
            new_name='title',
        ),
    ]
