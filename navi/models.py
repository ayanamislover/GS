from django.db import models

class Checker(models.Model):
    # create a primary key for the model
    id = models.AutoField(primary_key=True)
    # latitude, using DecimalField to store precise decimal and specify the maximum number of digits and decimal places
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    # longitude, using DecimalField to store precise decimal and specify the maximum number of digits and decimal places
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    # location name, using CharField to store a string with a maximum length of 255 characters
    location_name = models.TextField(default='Beautiful name')
    # tag, using CharField to store a string with a maximum length of 255 characters
    tag = models.CharField(max_length=255, default='question')
    # picture, using ImageField to store an image file
    picture = models.TextField(default='navi/static/images/Journey-amico.png')
    # overview, using TextField to store a large text field
    overview = models.TextField(default='Beautiful spot')

class player_profile(models.Model):
    last_game_start = models.DateTimeField(null=True, blank=True)
    verified_locations_count = models.IntegerField(default=0)

    def __str__(self):
        return self.location_name
