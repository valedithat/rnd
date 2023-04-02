from django.views.generic import ListView
from .models import Article

from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy


class ArticleList(ListView):
    model = Article