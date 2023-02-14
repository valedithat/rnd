from django.contrib import admin
from django.urls import path
from . import views


urlpatters = [
    path('', UserListView),
    path('/<int:pk>/]', UserDetailView),
    path('/new', UserCreateView),
    path('/edit', UserUpdateView),
    path('/delete', UserDeleteView)
]