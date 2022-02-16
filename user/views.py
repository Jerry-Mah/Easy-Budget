from django.shortcuts import redirect, render
from .models import Profile
from budget.forms import editUserForm
from budget.models import Sheet
from .models import ItemClone
from budget.forms import ItemForm

# Create your views here.


def userProfile(request):
    user = request.user
    profile = Profile.objects.get(user = user)
    context = {'profile':profile}
    return render(request, 'user/profile.html',context)


def editUser(request):
    user = request.user
    form = editUserForm(instance = user.profile)
    context = {'form':form}
    if request.method == "POST":
        form = editUserForm(request.POST, request.FILES,instance=user.profile)
        if form.is_valid:
            form.save()
            return redirect('profile')

    return render(request, "user/edit-user.html",context)

def delete(request,pk):
    sheet = Sheet.objects.get(id = pk)
    if request.method == "POST":
        sheet.delete()
        return redirect('profile')
    context = {'item':sheet}
    return render(request,'budget/delete-template.html',context)


def sheetView(request,pk):
    sheet1 = Sheet.objects.get(id = pk)

    context={"id": pk,"title":sheet1.name}
    return render(request,'user/sheet.html',context)


def deleteItem(request, pk):
    item = ItemClone.objects.get(id= pk)
    
    if request.method == "POST":
        item.delete()
        return redirect('profile')
    context = {'item':item}
    return render(request,'budget/delete-template.html',context)   