from django.db import models
from django_countries.fields import CountryField
CHOICES = [('M', 'Male'), ('F', 'Female')]

class Survey(models.Model):
    id = models.AutoField(primary_key=True)
    heard_of_cryptocurrency = models.BooleanField(default=False)
    purchased_cryptocurrency = models.BooleanField(default=False)
    consider_valid = models.BooleanField(default=False)
    advertisement_as_monetization = models.IntegerField(default=False)
    is_mobile = models.BooleanField(default=False)
    mining_intensity = models.IntegerField(default=False)
    performance_hits = models.IntegerField(default=False)
    experience = models.IntegerField(default=False)
    consider_solution = models.IntegerField(default=False)
    sex = models.CharField(default=False, choices=CHOICES, max_length=200)
    age = models.IntegerField(default=False)
    country = CountryField(default=False)
    time_spent = models.CharField(default=False, max_length=10000)
    total_hashes = models.CharField(default=False, max_length=10000)


