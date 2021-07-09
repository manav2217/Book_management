from django.contrib import admin
from django.urls import path , include
from . import views
from .views import  IndexView

urlpatterns = [
    path('' , IndexView.as_view() , name = "index"),
    path('AddBook/' , views.add_book , name = "AddBook"),

]