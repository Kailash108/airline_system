from enum import unique
from django.db import models

# Create your models here.

class Flightdetails(models.Model):
    Fnumber= models.CharField(unique=True, max_length=10)
    coname= models.TextField()
    fromdestination=models.TextField()
    todestination=models.TextField()
    nooftickets=models.IntegerField()
    boardingTime = models.TimeField(blank=True, null=True)
    arrivalTime = models.TimeField(blank=True, null=True)
    flight_fare = models.FloatField(blank=True,null=True)

class leaves(models.Model):
    Username=models.TextField()
    User_Id=models.CharField(unique=True,max_length=20)
    Mobile=models.IntegerField()
    Email=models.EmailField()
    Start_date=models.DateField()
    End_date=models.DateField()
    comments=models.TextField()   


class payment(models.Model):
    Name_on_Card =models.TextField()
    CardNumber =models.IntegerField(max_length=16,unique=True)
    ExpDate=models.DateField()
    cvv=models.IntegerField(max_length=3)
    
    
