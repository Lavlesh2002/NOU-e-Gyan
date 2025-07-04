from django.db import models

# Create your models here.
class Feedback(models.Model):
    fid=models.AutoField(primary_key=True)
    fdesc=models.CharField(max_length=200)

class Response(models.Model):
    id=models.AutoField(primary_key=True)
    roll_no=models.CharField(max_length=25)
    name=models.CharField(max_length=20)    
    program=models.CharField(max_length=50)    
    branch=models.CharField(max_length=50)    
    year=models.CharField(max_length=50)   
    number=models.CharField(max_length=10)   
    email=models.CharField(max_length=50)   
    restype=models.CharField(max_length=50)   
    subject=models.CharField(max_length=500)   
    responsetext=models.CharField(max_length=1000)   
    responsedate=models.DateField(auto_now_add=True)

class Question(models.Model):
    qid=models.AutoField(primary_key=True)
    que=models.CharField(max_length=50)
    desc=models.CharField(max_length=200)    
    created_by=models.CharField(max_length=30)
    created_date=models.DateField(auto_now_add=True)