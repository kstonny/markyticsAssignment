from django.db import models

# Create your models here.

class Reportform(models.Model):
    location_1 = models.CharField(max_length=80, blank=False, default='')
    location_2 = models.CharField(max_length=80,blank=False, default='')
    discription = models.CharField(max_length=80,blank=False, default='')
    date = models.DateField()
    time = models.TimeField()
    severity = models.CharField(max_length=80, blank=False, default='')
    casue = models.CharField(max_length=80, blank=False, default='')
    action = models.CharField(max_length=80, blank=False, default='')
    type_env = models.BooleanField(default=False)
    type_inj = models.BooleanField(default=False)
    type_prop = models.BooleanField(default=False)
    submitted =  models.BooleanField(default=False)
    reported_by = models.CharField(max_length=80,blank=False, default='')
    submitted_user = models.CharField(max_length=80,blank=False, default='')

