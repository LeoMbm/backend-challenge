from django.contrib import admin
from django.urls import path, include

from users import views

urlpatterns = [
   path('', views.getHome, name='home'),
   path('registration/', views.registerPage, name='registration'),
   path('login/', views.loginPage, name='login')

]
