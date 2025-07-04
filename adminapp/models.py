from django.db import models

# Create your models here.
class News(models.Model):
    nid=models.AutoField(primary_key=True)
    ntitle=models.CharField(max_length=20)
    ndesc=models.CharField(max_length=200)
    ndate=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=5)

class Program(models.Model):
    pid=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=20)
    pdate=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=5)
class Branch(models.Model):
    bid=models.AutoField(primary_key=True)
    bname=models.CharField(max_length= 50)
    bdate=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=5) 
class Year(models.Model):
    yid=models.AutoField(primary_key=True)
    yname=models.CharField(max_length=50)
    ydate=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=5)     

class Material(models.Model):
    id=models.AutoField(primary_key=True)
    program=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    file_name=models.CharField(max_length=100)
    my_file=models.FileField(upload_to='material/', max_length=100)
    status=models.CharField(max_length=5)