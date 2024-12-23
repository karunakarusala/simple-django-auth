from django.db import models

# Create your models here.
class Destination(models.Model) :
    image = models.ImageField(upload_to='pics')
    name  = models.CharField(max_length=100)
    price = models.IntegerField()
    description=models.TextField()
    offer = models.BooleanField(default=False)
