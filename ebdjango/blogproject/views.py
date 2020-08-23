from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

# Create your views here.


def home(request):
    blogs = Blog.objects
    return render(request, 'blogproject/home.html', {'blogs': blogs})


def helloworld(request):
    return render(request, 'blogproject/helloworld.html')
