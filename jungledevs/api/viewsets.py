from rest_framework import viewsets
from jungledevs.api import serializers
from jungledevs import models
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.db.models.functions import Lower
from rest_framework.filters import SearchFilter
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ArticlesSerializer, NotAuthenticatedArticlesSerializer


# from .serializers import ArticlesSerializer, NotAuthenticatedArticlesSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.AuthorSerializer
    queryset = models.Author.objects.all()


class ArticlesViewSet(viewsets.ModelViewSet):                                 # Admin
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.ArticlesSerializer
    queryset = models.Articles.objects.all()
    filterset_fields = ['category']

    # def get_serializer_class(self):
    #     if self.request.user.is_authenticated:
    #         return ArticlesSerializer
    #     else:
    #         return NotAuthenticatedArticlesSerializer


class AnonymousArticlesViewSet(viewsets.ModelViewSet):                        # Logout User
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = models.Articles.objects.all()
    filterset_fields = ['category']

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return ArticlesSerializer
        else:
            return NotAuthenticatedArticlesSerializer

   