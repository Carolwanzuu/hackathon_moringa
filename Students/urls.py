from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_groups/', views.group, name='group'),
    path('new-group/', views.create_group, name='new-group'),
]