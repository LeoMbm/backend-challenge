from django.contrib import admin
from django.urls import path, include

from logs import views

urlpatterns = [
    path('', views.getIpData, name='ip_index'),
    # path('all/', views.registerPage, name='registration'),

]

