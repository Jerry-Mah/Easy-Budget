from dataclasses import field
from django.forms import ModelForm
from .models import Item,Sheet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from django import forms
from user.models import Profile


class ItemForm(ModelForm):
    class Meta:
         model = Item
         fields = ['title', 'amount','tags']


class createUserForm(UserCreationForm):
    class Meta:
         model = User
         fields = ['first_name','email','username','password1', 'password2']
         labels= {
             'first_name':'Name',
         }

    
class editUserForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ['user']

class sheetForm(ModelForm):
    class Meta:
        model = Sheet
        fields = "__all__"
        exclude = ['user']



    
