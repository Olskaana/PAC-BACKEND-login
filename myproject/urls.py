"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path
from django.urls import include
from plano.views import criar_plano
from django.conf import settings
from django.conf.urls.static import static
from plano import views as plano_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('plano/', include('plano.urls')),
    path('', plano_views.index, name='index'),
    path('<str:municipio>/', plano_views.municipio, name='municipio'),
    path('<str:municipio>/criar-plano/', plano_views.criar_plano, name='criar_plano'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
