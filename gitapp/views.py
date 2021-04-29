from django.shortcuts import render, redirect
from .models import Content

def home(request):
    posts = Content.objects.all()
    return render(request, 'home.html', {'posts_list':posts})

# Create your views here.
