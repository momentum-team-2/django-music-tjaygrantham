from django.db import models

class Album(models.Model):
    artworkURL = models.URLField(max_length=255)
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    year = models.IntegerField()
    colors = models.CharField(null=True, blank=True, max_length=255)