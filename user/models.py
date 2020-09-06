from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    spotifyToken = models.CharField(blank=True, max_length=200)
    googleToken = models.CharField(blank=True, max_length=200)