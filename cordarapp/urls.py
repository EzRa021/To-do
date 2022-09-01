from django.contrib import admin
from django.urls import path,include
from . import views

app_name="cordarapp"                      
urlpatterns = [
   # path('', views.index, name="index"),
   path('', views.home, name="home"),
#    path('admin/', views.admin, name="admin"),
   path('dash/', views.dash, name="dash"),
   path('edit/<int:id>', views.edit, name="edit"),
   path('delete/<int:id>', views.delete, name="delete"),
   path('pricing/', views.pricing, name="pricing"),
   path('services/', views.services, name="services"),

]
