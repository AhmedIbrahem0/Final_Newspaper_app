from .views import ArticleListView,ArticleDetail,ListUserApiView,ListDetail
from django.urls import path
urlpatterns=[
    path("article/",ArticleListView.as_view()),        #? Read and create articles     
    path("article/<int:pk>/",ArticleDetail.as_view()) ,#? update and delete articles
    path("users/",ListUserApiView.as_view()),          #? Read and create Users      
    path("users/<int:pk>/",ListDetail.as_view())       #? update and delete Users
]