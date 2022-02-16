from django.urls import path,include
from . import views
# from budget.urls import *

urlpatterns = [
    path('', views.userProfile, name='profile'),
    path('sheet-view/<str:pk>', views.sheetView, name = 'sheet'),

    path('delete-item/<str:pk>', views.deleteItem, name = 'delete-item'),

    path('delete-sheet/<str:pk>', views.delete, name = 'delete-sheet'),
    path('edit-user/', views.editUser, name= 'edit-user')
    
]
