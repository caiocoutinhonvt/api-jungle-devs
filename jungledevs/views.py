from django.shortcuts import render
from django.contrib.auth.models import User
from jungledevs.api.serializers import RegisterSerializer
from rest_framework import generics
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .documents import AuthorDocument, ArticleDocument
from .api.serializers import AuthorSerializer, ArticlesSerializer
from django_elasticsearch_dsl_drf.filter_backends import FilteringFilterBackend, CompoundSearchFilterBackend

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer



class AuthorDocumentView(DocumentViewSet):
    document = AuthorDocument
    serializer_class = AuthorSerializer

    filter_backends = [
        FilteringFilterBackend,
        CompoundSearchFilterBackend
    ]

    search_fields= ('name', 'pictures')
    multi_match_search_fields= ('name', 'pictures')
    filter_fields = {
        'name':'name',
        'pictures':'pictures'
      
    }


class ArticleDocumentView(DocumentViewSet):
    document = ArticleDocument
    serializer_class = ArticlesSerializer

    filter_backends = [
        FilteringFilterBackend,
        CompoundSearchFilterBackend
    ]

    search_fields= ("id", "author_id", "author", "category",
                  "title", "summary", "firstParagraph", "body")
    multi_match_search_fields= ("id", "author_id", "author", "category",
                  "title", "summary", "firstParagraph", "body")
    filter_fields = {
        "id":"id",
        "author_id": "author_id", 
        "author": "author",
        "category": "category",
        "title":"title",
        "summary":"summary",
        "firstParagraph": "firstParagraph",
        "body": "body"
    }
    