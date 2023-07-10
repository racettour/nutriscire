from django.db import models
from django.utils import timezone
import datetime 


# Create your models here.

class produit(models.Model):
    id = models.CharField(primary_key=True)
    categories = models.TextField(max_length=5000)
    brands =  models.TextField(null=True)
    nutriscore_score = models.TextField(null=True)
    quantity = models.TextField(max_length=5000,null=True)
    nutriscore_grade  = models.TextField(max_length=200,null=True)
    

    

    