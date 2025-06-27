from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(default=18)
    father_name = models.CharField(max_length=100)