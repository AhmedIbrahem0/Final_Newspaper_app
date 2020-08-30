from django.views.generic import ListView ,CreateView  ,DetailView
from django.views.generic.edit import DeleteView,UpdateView
from .models import Article
from django.urls import reverse_lazy
class ArticleListView(ListView):
    model =Article
    template_name="article_list.html"
class ArticleDeleteView(DeleteView):
    template_name="article_delete.html"
    model=Article
    success_url=reverse_lazy("article_list")
class ArticleUpdatetView(UpdateView):
    template_name="article_edit.html"
    model=Article
    fields=("title","body")
class ArticleDetailteView(DetailView):
    template_name="article_detail.html"
    model=Article
class ArticleCreateView(CreateView):
    model=Article
    template_name="article_new.html"
    fields=("title","auther","body")
    