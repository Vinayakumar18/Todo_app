from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
appname='Todo'
urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.add, name="add"),
    path('check/<todo_id>', views.check, name="check"),
    path('uncheck/<todo_id>', views.uncheck, name="uncheck"),
    path('deletecomplete', views.deletecomplete, name="deletecomplete"),
    path('deleteall',views.deleteall, name="deleteall"),
]