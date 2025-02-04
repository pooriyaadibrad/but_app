from django.urls import path

from butapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register_'),
    path('follow/', views.follow , name='follow'),
    path('terms_and_conditions/', views.terms_and_conditions , name='terms_and_conditions'),
    path('detail/<int:but_id>/', views.detail, name='detail')
]
