from django.shortcuts import render
from .serializer import *
from rest_framework import generics,filters
from .models import *
from django_filters.rest_framework import DjangoFilterBackend


class BookListView(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    filter_backends=(DjangoFilterBackend, filters.SearchFilter,)
    filterset_fields=['year_of_issue','author']
    search_fields=['title']
 
class BookCreateView(generics.CreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

 
class BookUpdateView(generics.UpdateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

 
class BookDeleteView(generics.DestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

 

class AuthorListView(generics.ListAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

 
class AuthorCreateView(generics.CreateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

 
class AuthorUpdateView(generics.UpdateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

 
class AuthorDeleteView(generics.DestroyAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

 