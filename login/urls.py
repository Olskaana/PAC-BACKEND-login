# login/urls.py
from django.urls import path
from .views import RegisterView, get_csrf_token, login_view
#from plano.views import index

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='api-register'),
    path('api/csrf/', get_csrf_token, name='api-csrf-token'),
    path('api/login/', login_view, name='api-login'),
]
