from django.db import models
from django.db.models.base import ModelState
from django.db.models.fields import EmailField

# Create your models here.
class Product (models.Model):
    
    # sku = models.CharField(max_length=10 , primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    # prices less than 9999.99
    price = models.DecimalField(max_digits=6 , decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)


class Customer (models.Model):

    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE , 'Bronze'),
        (MEMBERSHIP_SILVER , 'Silver'),
        ( MEMBERSHIP_GOLD , 'Gold'),
    ]

    first_name =  models.CharField(max_length=255)
    last_name =  models.CharField(max_length=255)
    email =  models.EmailField(unique=True)
    phone =  models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1 , choices=MEMBERSHIP_CHOICES , default=MEMBERSHIP_BRONZE)


class Order (models.Model):

    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS = [
        (   PAYMENT_STATUS_PENDING , 'pending'),
        (   PAYMENT_STATUS_COMPLETE     , 'complete'),
        (   PAYMENT_STATUS_FAILED , 'failed'),
    ]
    
    placed_at = models.DateField(auto_now_add=True)
    payment_status = models.CharField(max_length=1 , choices=PAYMENT_STATUS)

