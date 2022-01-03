from django.shortcuts import render,redirect
from .forms import ItemForm
from .models import Item

# Create your views here.

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