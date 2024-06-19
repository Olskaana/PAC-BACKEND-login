# urls.py
from django.urls import path
from .views import criar_plano
from . import views

urlpatterns = [
    path('<str:municipio>/criar-plano/', views.criar_plano, name='criar_plano'),
]
