from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.models import User
# Create your views here.

def userProfile(request,pk):
    profile = Profile.objects.get(id = pk)
    context = {'profile':profile}
    return render(request, 'user/profile.html',context)