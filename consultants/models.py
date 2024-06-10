from django.db import models
from django.contrib.auth.models import AbstractUser
from customer.models import CustomUser

# Create your models here.

class Skill(models.Model):
    
    name = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    level = models.SmallIntegerField()
  
    def __str__(self):
        return self.name


class Expert(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='expert')
    skills = models.ManyToManyField(Skill, related_name='experts')
    start_date = models.DateField(null=True)


