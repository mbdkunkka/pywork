from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('login/', views.login, name='login'),
    path('detail/', views.detail, name='detail'),
]