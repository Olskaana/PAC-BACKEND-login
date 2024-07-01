from django.urls import path
from .views import CriarPlanoAPIView, MunicipioAPIView, PlanoDetailAPIView, EditarPlanoAPIView

urlpatterns = [
    path('api/<str:municipio>/criar-plano/', CriarPlanoAPIView.as_view(), name='criar_plano'),
    path('api/municipios/<str:municipio>/', MunicipioAPIView.as_view(), name='listar-planos'),
    path('api/municipios/<str:municipio>/planos/<int:id_plano>/', PlanoDetailAPIView.as_view(), name='detalhar-plano'),
    path('api/municipios/<str:municipio>/planos/<int:id_plano>/editar/', EditarPlanoAPIView.as_view(), name='editar-plano'),
]
