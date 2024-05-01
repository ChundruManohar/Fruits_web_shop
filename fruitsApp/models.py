from django.db import models

# Create your models here.
class Fruit(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()    
    
    def __str__(self):
        return self.name