from django.contrib import admin
from django.urls import path,include
from . import views

app_name ="usersapp"
       
urlpatterns = [
   path('register/', views.register, name="register"),
   path('login/', views.login, name="login"),
   path('logout/', views.exits, name="logout"),
]
