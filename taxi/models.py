from django.db import models

# Create your models here.


class Car(models.Model):
    grz = models.CharField(unique=True, null=False)
    model = models.CharField(max_length=10)
    owner = models.CharField(max_length=5)
    fuel_type = models.CharField(max_length=5)
    lease_payment = models.DecimalField(decimal_places=2, null=True)
    mileage = models.IntegerField(null=True)
