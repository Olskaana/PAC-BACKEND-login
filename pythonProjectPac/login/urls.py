# login/urls.py
from django.urls import path
from .views import login_view, login_success, register_view
from plano.views import index

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('success/', login_success, name='success'),
    path('', index, name='index'),
]
