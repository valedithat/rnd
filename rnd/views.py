from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy

from django.http import HttpResponse

def rnd(request):
    return HttpResponse("Hello, world. Welcome to RND.")
