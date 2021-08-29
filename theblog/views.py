from theblog.models import Post
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Post

# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

# def HomeView(request):
#     return render(request, 'home.html')

class ArticleDetailView(DetailView):
    model = Post
    template = 'post_detail.html'

