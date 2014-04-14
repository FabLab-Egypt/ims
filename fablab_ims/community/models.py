from django.db import models
from django.contrib.auth.models import User

class IMS_Manager(models.Model):
    user = models.ForeignKey(User, unique=True)

class Character(models.Model):
    name      = models.CharField(max_length = 100, verbose_name = "Full Name")
    email     = models.CharField(max_length = 100, verbose_name = "email")
    mobile    = models.CharField(max_length = 20, verbose_name = "mobile")
    birhtdate = models.DateField(auto_now=False, auto_now_add=False)
    # professsion
    
class Member(Character):
    member_id = models.CharField(max_length = 40, verbose_name = "Member ID") # sha1(email;yyyy.mm.dd;mobile)

class Volunteer(Member):
    pass

class Visitor(Character):
    pass