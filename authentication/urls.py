from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginUser, name='login'),
     path('signup/', views.signupUser, name='signup'),
    path('logout/', views.logoutUser, name='logout'),
]
