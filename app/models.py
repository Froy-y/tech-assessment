from django.db import models
from django.urls import reverse
from datetime import datetime, timedelta

# Create your models here.
class Listing(models.Model):
    name = models.CharField(max_length=20)
    # Add a way to store a listing's street address ZIP code
    address = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    # Add a way to store common amenities sometimes provided by a listing
    amenities = models.TextField(max_length=150)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("listing_details", kwargs={"pk": self.id})
    
class Reservation(models.Model):
    name = models.CharField(max_length=50)
    # Add a way to store “check-in” and “check-out” dates for reservations
    check_in = models.DateTimeField(default=datetime.now(), blank=True,)
    check_out = models.DateTimeField(default= datetime.now() + timedelta(days=1), blank=True)
    # Add a way to link reservations and listings
    listing = models.ManyToManyField(Listing)
    
    def date_difference(self):
        if self.check_in: 
            timediff = self.check_out - self.check_in
            return timediff
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('reservation_details', kwargs={'reservations_id': self.id})
    
