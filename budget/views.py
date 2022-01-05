from django.shortcuts import render,redirect
from .forms import ItemForm
from .models import Item
from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    items = Item.objects.filter(user = request.user)
    form = ItemForm()
    total = 0
    for item in items:
        total += int(item.amount)
    if request.user.is_authenticated:
        if request.method == "POST":
            user = request.user
            form = ItemForm(request.POST)
            if form.is_valid:
                itemList = form.save(commit=False)
                itemList.user = user
                itemList.save()
                
                return redirect('home')

    context = {'form':form, 'items':items,'total':total}
    
    return render(request,'budget/home.html',context)

@login_required
def update(request, pk):
    item = Item.objects.get(id= pk)
    form = ItemForm(instance = item)

    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid:
            form.save()
            return redirect('home')

    context = {'item':item, 'form':form}
    return render(request,'budget/update-template.html',context)

@login_required
def delete(request, pk):
    item = Item.objects.get(id= pk)
    
    if request.method == "POST":
        item.delete()
        return redirect('home')
    context = {'item':item}
    return render(request,'budget/delete-template.html',context)    