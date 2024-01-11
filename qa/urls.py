from django.contrib import admin
from django.urls import path, include
from qa import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/',views.form,name='fillform'),
    path('showform/',views.get_form,name='getfrom'),
    path('delete/',views.delete,name='getfrom'),
    path('bookform/',views.book_form,name='book'),
    path('booklist/',views.BooksListView.as_view(),name='book')
]