from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy

from django.http import HttpResponse

def articles(request):
    return HttpResponse("Articles and Shit")