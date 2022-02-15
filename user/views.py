from django.core.checks import messages
from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponse
from .models import Profile
from django.contrib import messages
from django.contrib.auth.models import User
from budget.forms import editUserForm
from budget.models import Sheet

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
    context={}
    return render(request,'user/sheet.html',context)