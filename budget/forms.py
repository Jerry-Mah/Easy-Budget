from django.forms import ModelForm
from .models import Item
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ItemForm(ModelForm):
    class Meta:
         model = Item
         fields = ['title', 'amount','tags']


class createUserForm(UserCreationForm):
    class Meta:
         model = User
         fields = ['username', 'email', 'password1', 'password2']