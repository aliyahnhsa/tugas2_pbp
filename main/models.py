from django.db import models

class GamesEntry(models.Model):
    name = models.CharField()
    price = models.IntegerField()
    description = models.TextField()
