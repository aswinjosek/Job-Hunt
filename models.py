from django.db import models

# Create your models here.
class Admindb(models.Model):
    firstname=models.CharField(max_length=20,null=True,blank=True)
    lastname=models.CharField(max_length=20,null=True,blank=True)
    email=models.CharField(max_length=20,null=True,blank=True)
    username=models.CharField(max_length=20,null=True,blank=True)
    password=models.CharField(max_length=20,null=True,blank=True)
    confirmpassword=models.CharField(max_length=20,null=True,blank=True)
    
    
