from email import message
from tkinter import Widget
from django.db import models

# Create your models here.
class new_user(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length = 254)
    password=models.CharField(max_length=34)
    

    def __str__(self):
        return self.username

class contact(models.Model):
    name=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=250)
    email=models.EmailField(max_length = 50)

    def __str__(self):
        return self.name
    