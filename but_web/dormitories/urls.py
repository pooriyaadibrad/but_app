from django.urls import path

from dormitories import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
]