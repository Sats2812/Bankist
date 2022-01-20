from email import message
from tkinter import CASCADE, Widget
from unicodedata import name
from django.db import models

# Create your models here.
class new_user(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length = 254)
    password=models.CharField(max_length=34)
    balance=models.IntegerField(max_length=8,default=0)
    debitcard_holder=models.BooleanField(default=False)

    def __str__(self):
        return self.username

class contact(models.Model):
    name=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=250)
    email=models.EmailField(max_length = 50)

class Loan(models.Model):
    amount=models.BigIntegerField()
    uid=models.ForeignKey(new_user,on_delete=models.CASCADE)

class Transaction(models.Model):
    fromid=models.ForeignKey(new_user,on_delete=models.CASCADE,related_name='fromid')
    toid=models.ForeignKey(new_user,on_delete=models.CASCADE,related_name='toid')
    amount=models.IntegerField(max_length=5)

class Debitcard(models.Model):
    userid=models.ForeignKey(new_user,on_delete=models.CASCADE)
    card_no=models.CharField(max_length=16)
    cvv=models.CharField(max_length=3)
    