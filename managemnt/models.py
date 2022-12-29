from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from enum import Enum

class TransactionStatus(models.TextChoices):
    HR = "HR"
    USER = "USER"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type_of_user = models.TextField(choices=TransactionStatus.choices, default=TransactionStatus.USER)
    belongs_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='belongs_to_which_hr')


class InventoryItem(models.Model):
    name = models.CharField(max_length=30)
    belongs_to = models.ForeignKey(Profile, on_delete = models.CASCADE)
    availablity = models.BooleanField(default=True)


class ItemProfileMapping(models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    item = models.ForeignKey(InventoryItem, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)