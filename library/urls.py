"""library URL Configuration

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
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from jungledevs.views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import routers
from jungledevs.api import viewsets as jungledevsviewsets 
from rest_framework_swagger.views import get_swagger_view

route = routers.DefaultRouter()

# schema_view = get_swagger_view(title= "Jungle Devs")

route.register(r'api/admin/authors', jungledevsviewsets.AuthorViewSet, basename="Author")
route.register(r'api/admin/articles', jungledevsviewsets.ArticlesViewSet, basename="ArticlesAdmin")
route.register(r'api/admin/articles', jungledevsviewsets.ArticlesViewSet, basename="Articles")
route.register(r'api/articles', jungledevsviewsets.AnonymousArticlesViewSet, basename="AnonymousArticles")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/login/refresh/', TokenRefreshView.as_view()), 
    path('api/sign-up/', RegisterView.as_view(), name='auth_register'),
    # path('', schema_view)


    *static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
]
