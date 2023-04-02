from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.ArticleList.as_view(), name='articles'),
]