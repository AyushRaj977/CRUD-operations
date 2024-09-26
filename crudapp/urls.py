from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('home/',home),
    path('add_student',std_add),
    path('delete_stdudent<int:roll>',std_delete),
    path('update_stdudent<int:roll>',std_update),
    path('do_update_stdudent<int:roll>',do_std_update),
]