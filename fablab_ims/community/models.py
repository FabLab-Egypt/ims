from django.db import models
from django.contrib.auth.models import User

class IMS_Managers(models.Model):
    user = models.ForeignKey(User, unique=True)

class Characters(models.Model):
    name      = models.CharField(max_length = 100, verbose_name = "Full Name")
    email     = models.CharField(max_length = 100, verbose_name = "email")
    mobile    = models.CharField(max_length = 20, verbose_name = "mobile")
    birhtdate = models.DateField(auto_now=False, auto_now_add=False)
    # professsion
    
    
