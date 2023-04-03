from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Article

from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy


class ArticleList(ListView):
    model = Article


class ArticleDetail(DetailView):
    model = Article