from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
     path('logout/', views.logoutUser, name='logout'),

    path('', views.home, name='home'),
    path('update/<str:pk>', views.update, name='update-item'),
    path('delete/<str:pk>', views.delete, name='delete-item'),
]
