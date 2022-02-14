from django.urls import path
from . import views


urlpatterns = [
    path('', views.userProfile, name='profile'),
    path('sheet-view/<str:pk>', views.sheetView, name = 'sheet'),

    path('delete-sheet/<str:pk>', views.delete, name = 'delete-sheet'),
    path('edit-user/', views.editUser, name= 'edit-user')
    
]
