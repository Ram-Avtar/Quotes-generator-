from django.db import models
from django.contrib.auth.models import User



class Quotes(models.Model):
	sn=models.CharField(max_length=20)
	content=models.TextField()
	auther=models.CharField(max_length=50)

def __str__(self):
	return self.sn



# Create your models here.
