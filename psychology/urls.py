from django.urls import path
from . import views

urlpatterns = [
    path('', views.psychology, name='home'),
    path('create_case/', views.create_case, name='create_case'),
]