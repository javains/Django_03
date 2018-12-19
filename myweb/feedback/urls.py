
from django.contrib import admin
from django.urls import path
from feedback import views

urlpatterns = [
     path('add/', views.add,name='add'),
     path('list/', views.list,name='list'),
     path('edit/(?P<id>\d+)/$', views.edit,name='edit'),

]
