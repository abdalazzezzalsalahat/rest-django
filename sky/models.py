from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Sky(models.Model):
    name = models.CharField(max_length=256)
    discription = models.TextField()
    architect = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
