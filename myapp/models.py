from django.db import models

# Create your models here.

class passenger(models.Model):  
    passenger_name = models.CharField(max_length=50)  
    passport_number = models.CharField(max_length=30)
    dept_airport = models.CharField(max_length=50)  
    arrive_airport = models.CharField(max_length=30)
    flight_number = models.CharField(max_length=30)
    url_image = models.CharField(max_length=255, default="")
    class Meta:  
        db_table = "passenger_tbl"

