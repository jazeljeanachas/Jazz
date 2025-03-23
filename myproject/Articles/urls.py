from django.urls import path
from .views import ArticleListCreate, ArticleRetrieveUpdateDestroy  

urlpatterns = [
    path('article/', ArticleListCreate.as_view(), name='article-list'),
    path('article/<int:pk>/', ArticleRetrieveUpdateDestroy.as_view(), name='article-detail'),
]
