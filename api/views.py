from rest_framework import generics
from .serializer import UserSerizlezier,ArticleSerializer
from users.models import CustomUser
from articles.models import Article
#? users Api View
class ListUserApiView(generics.ListCreateAPIView):
    serializer_class= UserSerizlezier
    queryset= CustomUser.objects.all()
class ListDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class= UserSerizlezier
    queryset= CustomUser.objects.all()

#? Article Api View
class ArticleListView(generics.ListCreateAPIView):
    serializer_class=ArticleSerializer
    queryset=Article.objects.all()
class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=ArticleSerializer
    queryset=Article.objects.all()