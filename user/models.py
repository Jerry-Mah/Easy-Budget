from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

import uuid
from django.dispatch import receiver
from budget.models import Tag

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null =True, blank = True)
    username= models.CharField(max_length=200, blank = True, null = True)
    name = models.CharField(max_length=200, blank = True, null = True)
    email = models.EmailField(max_length=500, blank = True, null=True)
    bio = models.TextField(blank = True, null = True)
    profile_image = models.ImageField(null = True, blank = True,default = 'user-default.png')
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique = True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.user.username)

class ItemClone(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null = True,related_name="itemOwnerClone")
    title = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10000, decimal_places=2)
    tags = models.ForeignKey(Tag,null = True,on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique = True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


