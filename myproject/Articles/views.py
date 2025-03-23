from django.shortcuts import render
from rest_framework import generics
from .models import Post  
from .serializers import ArticleSerializer 

class ArticleListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all() 
    serializer_class = ArticleSerializer

class ArticleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all() 
    serializer_class = ArticleSerializer
