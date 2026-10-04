from django.shortcuts import render
from .pagination import StandardPagination
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class=StandardPagination
    queryset=Book.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=BookSerializer
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields=["author","published_year"]
    search_fields=["title","author","description"]
    ordering_fields=["title","published_year","created_at"]
    ordering=["-created_at"]