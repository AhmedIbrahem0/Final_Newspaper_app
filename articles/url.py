from .views import ArticleListView , ArticleCreateView ,ArticleDeleteView ,ArticleUpdatetView ,ArticleUpdatetView
from django.urls import path
urlpatterns=[
    path("",ArticleListView.as_view(),name='article_list'),
    path("<int:pk>/delete/",ArticleDeleteView.as_view(),name="article_delete"),
    path("<int:pk>/edit/",ArticleUpdatetView.as_view(),name="article_edit"),
    path("new/",ArticleCreateView.as_view(),name="article_new"),
    path("<int:pk>",ArticleDeleteView.as_view(),name="article_detail")


]