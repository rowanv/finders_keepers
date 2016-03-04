from django.db import models

class Location(models.Model):

    lat = models.FloatField()
    lon = models.FloatField()
    address = models.CharField(max_length=400)

    def __str__(self):
        return self.lat + ', ' + self.lon + ' ' + self.address