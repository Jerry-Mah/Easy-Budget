from django.shortcuts import render,redirect
from .forms import ItemForm
from .models import Item
from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def loginUser(request):
    # if request.user.is_authenticated:
    #     return redirect('home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)
            print(user)
        except:
            messages.error(request, "Username does not exist")

        user = authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)
            messages.error(request, "Successfully loged in")
            return redirect('home')
        else:
            messages.error(request, "Username or password is incorrect")
        
    
    return render(request, "budget/login_register.html")

def logoutUser(request):
    logout(request)
    messages.error(request, "Successfully logged out")
    return redirect('login')

def home(request):
    items = Item.objects.all()
    form = ItemForm()
    total = 0
    for item in items:
        total += int(item.amount)
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid:
            form.save()
            
            return redirect('home')

    context = {'form':form, 'items':items,'total':total}
    print(request.user)
    return render(request,'budget/home.html',context)

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

def delete(request, pk):
    item = Item.objects.get(id= pk)
    
    if request.method == "POST":
        item.delete()
        return redirect('home')
    context = {'item':item}
    return render(request,'budget/delete-template.html',context)    