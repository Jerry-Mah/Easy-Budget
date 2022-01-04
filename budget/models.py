from django.contrib.auth.models import User
from django.db import models
import uuid

from django.db.models.deletion import DO_NOTHING
from django.utils import tree

# Create your models here.

class Item(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null = True,related_name="itemOwner")
    title = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10000, decimal_places=2)
    tags = models.ForeignKey('Tag',null = True,on_delete=DO_NOTHING)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique = True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length= 200)
    created = models.DateTimeField(auto_now = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True , primary_key=True, editable=False)

    def __str__(self):
        return self.name
