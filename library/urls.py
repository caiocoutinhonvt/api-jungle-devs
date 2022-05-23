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
from jungledevs.api import viewsets as  views


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Jungle Devs - Challenge",
      default_version='v1',
     
     
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



route = routers.DefaultRouter()

route.register(r'api/admin/authors', views.AuthorViewSet, basename='Author')
route.register(r'api/admin/articles', views.ArticlesViewSet, basename='ArticlesAdmin')
route.register(r'api/admin/articles', views.ArticlesViewSet, basename='Articles')
route.register(r'api/articles', views.AnonymousArticlesViewSet, basename='AnonymousArticles')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/login/refresh/', TokenRefreshView.as_view()), 
    path('api/sign-up/', RegisterView.as_view(), name='auth_register'),
    # path('1/', schema_view),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), 
    *static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
]

# urlpatterns += [
#    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
#    ...
# ]

