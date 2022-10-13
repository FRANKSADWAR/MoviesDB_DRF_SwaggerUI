from django.db import models


class Movies(models.Model):
    name = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=90,decimal_places=2)
    release_date = models.DateField()
    description = models.CharField(max_length=200)
    staring = models.TextField(max_length=500)

    class Meta:
        verbose_name_plural = 'Movies'
    def __str__(self):
        return '%s %s'.format(self.name, self.description)

class Songs(models.Model):
    name = models.CharField(max_length=100)
    artists = models.TextField(max_length=500)
    sold = models.IntegerField()
    date = models.DateField()

    class Meta:
        verbose_name_plural = 'Songs'

    def __str__(self):
        return '%s %s'.format(self.name, self.artists)