from django.shortcuts import render,redirect
from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.models import User
from budget.forms import createUserForm

# Create your views here.
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            try:
                user = User.objects.get(username = username)
                
            except:
                messages.error(request, "Username does not exist")

            user = authenticate(request, username= username, password= password)
            if user is not None:
                login(request, user)
                messages.error(request, "Successfully loged in")
                return redirect('home')
            else:
                messages.error(request, "Username or password is incorrect")
        
    
    return render(request, "authentication/login_register.html")

def logoutUser(request):
    logout(request)
    messages.error(request, "Successfully logged out")
    return redirect('login')


def signupUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = createUserForm()
        if request.method == "POST":
            form = createUserForm(request.POST)
            if not form.is_valid():
                messages.error(request,"Some errors occured. Try again.")
                context = {'form':form, 'form_errors':form.errors}
                return render(request, "authentication/signup.html", context)
            elif form.is_valid():
                user = form.save(commit = False)
                user.save()
                login(request,user)
                
                messages.success(request,"User successfuly created.")
                return redirect('login')
        
    context = {'form':form}
    return render(request, "authentication/signup.html",context)