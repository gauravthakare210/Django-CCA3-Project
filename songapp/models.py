from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=100)
    singer = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    
