# urls.py
from django.urls import path
from .views import criar_plano
from . import views
from plano import views as plano_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('<str:municipio>/criar-plano/', views.criar_plano, name='criar_plano'),
    path('', plano_views.index, name='index'),
    path('<str:municipio>/<int:id_plano>/', views.plano_detail, name='plano_detail'),
    #path('<str:municipio>/plano/<int:id_plano>/editar/', views.editar_plano, name='editar_plano'),
    path('<str:municipio>/plano/<int:id_plano>/excluir/', views.excluir_plano, name='excluir_plano'),
    # API Endpoints
    path('api/criar_plano/<str:municipio>/', views.criar_plano_api, name='criar_plano_api'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

