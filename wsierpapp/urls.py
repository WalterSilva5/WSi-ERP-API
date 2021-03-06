"""projetowsierp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path, include

from drf_spectacular.views import (SpectacularAPIView,
                                   SpectacularRedocView, SpectacularSwaggerView)
from wsierpapp.views import (
    usuario_view, produto_view, categoria_view, venda_view)
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    #swagger
    path('swagger-file/', SpectacularAPIView.as_view(), name='schema'),
    # redoc
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # swagger
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    #usuario
    path('api/usuario/', usuario_view.UsuarioViewSet.as_view(), name='usuario'),
    #login
    path('api/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    #index
    # re_path(r'', front_view.index, name='index'),
]