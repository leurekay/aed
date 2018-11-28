from __future__ import unicode_literals

from django.db import models
import datetime
import django.utils.timezone as timezone
# Create your models here.
 
 
class RGB(models.Model):
    uid = models.CharField(max_length=30,default='aaaaaa')
    timestamp = models.IntegerField(default=0)
    datetime = models.DateTimeField(default = timezone.now)
    R1 = models.IntegerField(default=-999)
    R1C= models.IntegerField(default=-999)  
    R2 = models.IntegerField(default=-999)
    R2C = models.IntegerField(default=-999)  
    G1 = models.IntegerField(default=-999)
    G1C = models.IntegerField(default=-999)  
    G2 = models.IntegerField(default=-999)
    G2C = models.IntegerField(default=-999)  
    B1 = models.IntegerField(default=-999)
    B1C = models.IntegerField(default=-999)  
    B2 = models.IntegerField(default=-999)
    B2C = models.IntegerField(default=-999)  