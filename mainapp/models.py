from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no=models.BigIntegerField(primary_key=True)
    name=models.CharField(max_length=35)
    fname=models.CharField(max_length=35)
    mname=models.CharField(max_length=35)
    gender=models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    program=models.CharField(max_length=20)
    branch=models.CharField(max_length=30)
    year=models.CharField(max_length=10)
    number=models.CharField(max_length=10)
    email=models.CharField(max_length=35)

class Login(models.Model):
    userid=models.CharField(max_length=30, primary_key=True)
    password=models.CharField(max_length=25)
    utype=models.CharField(max_length=10)
    status=models.CharField(max_length=10)

class Enquiry(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=20)
    address=models.CharField(max_length=255)
    contactno=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    enquirytext=models.CharField(max_length=255)
    enquirydate=models.DateField(auto_now_add=True)    