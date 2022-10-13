from django.db import models


class Movies(models.Model):
    name = models.CharField(max_length=100)
    budget = models.DecimalField()
    release_date = models.DateField()
    description = models.CharField(max_length=200)
    staring = models.TextField(max_length=500)

    def __str__(self):
        return 

class Songs(models.Model):
    name = models.CharField(max_length=100)
    artists = models.TextField(max_length=500)
    sold = models.IntegerField()
    date = models.DateField()