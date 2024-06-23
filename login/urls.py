# login/urls.py
from django.urls import path
from .views import login_view, login_success, register_view, delete_user, update_user, logout_view
from plano.views import index

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('success', login_success, name='success'),
    path('', index, name='index'),
    path('delete/', delete_user, name='delete_user'),
    path('update/', update_user, name='update_user'),
    path('logout/', logout_view, name='logout'),
]
