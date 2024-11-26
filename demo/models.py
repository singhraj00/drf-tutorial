from django.db import models

# Create your models here.

class New_Joinee(models.Model):
    tr_id = models.CharField(max_length=8)
    name = models.CharField(max_length=20)
    designation = models.CharField(max_length=12)
    stepined = models.IntegerField()

