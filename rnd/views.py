from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy

def rnd(request):
    return render(request, 'rnd.html')
