from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):
    brand=models.CharField(max_length=50)
    model=models.CharField(max_length=50)
    gear_type=models.CharField(max_length=50)
    fuel_type=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    year=models.IntegerField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return {
            'brand': self.brand,
            'model': self.model,
            'gear_type': self.gear_type,
            'fuel_type': self.fuel_type,
            'color': self.color,
            'year': self.year,
            'price': self.price,
            'user': self.user,
        }
    
class Image(models.Model):
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    img_url = models.ImageField(upload_to='')