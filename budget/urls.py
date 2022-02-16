from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sheet/',views.sheet,name = 'sheet'),
    # path('clear/',views.clear, name = "clear"),
    path('update/<str:pk>', views.update, name='update-item'),
    path('delete/<str:pk>', views.delete, name='delete-item')
]
