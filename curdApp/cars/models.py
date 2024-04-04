from django.db import models

# Create your models here.
class Cars(models.Model):
    care_name = models.CharField(max_length=100)
    car_version = models.CharField(max_length=3)
    car_model = models.CharField(max_length=30)

    def __str__(self):
        return self.care_name

# Create your models here.
