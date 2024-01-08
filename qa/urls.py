from django.contrib import admin
from django.urls import path, include
from qa import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/',views.form,name='fillform')
      path('form/',views.get_from,name='getfrom')
]