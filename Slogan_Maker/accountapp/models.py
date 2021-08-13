from django.db import models

# Create your models here.

class main_slogan(models.Model):
    content = models.CharField(max_length=255, null=False)
    date = models.DateField(auto_now=True)

class post(models.Model):
    select = models.CharField(max_length=100)
    info = models.CharField(max_length=20)
    sim = models.IntegerField()
