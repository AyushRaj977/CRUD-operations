from django.db import models

class Student(models.Model):
    roll=models.CharField(max_length=5)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    address=models.CharField(max_length=200)
    phone=models.PositiveIntegerField()
