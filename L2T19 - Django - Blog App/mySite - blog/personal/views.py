from django.shortcuts import render

def home(request):
    return render(request, 'personal/home.html')

def page1(request):
    return render(request, 'personal/page1.html')

def page2(request):
    return render(request, 'personal/page2.html')

from django.shortcuts import render
from .models import BlogPost  # Import your blog model

def blog_list(request):
    posts = BlogPost.objects.all()  # Get all blog posts
    return render(request, 'blog/blog_list.html', {'posts': posts})