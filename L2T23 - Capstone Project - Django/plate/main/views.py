from django.shortcuts import render, redirect
from .models import Skill
from .forms import SkillForm
from django.conf import settings

import os
base_dir = settings.BASE_DIR
from django.shortcuts import render
from django.conf import settings

def homepage(request):
    """
    Render the homepage template.

    Parameters:
    request (HttpRequest): The request object.

    Returns:
    HttpResponse: The rendered homepage template.
    """
    return render(request, 'main/homepage.html')



from django.shortcuts import render, redirect
from .forms import SkillForm  # Assuming you have a form named SkillForm

def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')  # Redirect to homepage after saving
    else:
        form = SkillForm()
    
    return render(request, 'main/add_skill.html', {'form': form})

from django.shortcuts import render

def skills_list(request):
    # Your logic to display the skills list
    return render(request, 'main/skills_list.html')


def contact(request):
    return render(request, 'main/contact.html')

def news(request):
    return render(request, 'main/news.html')

def register(request):
    return render(request, 'main/register.html')

def login_view(request):
    return render(request, 'main/login.html')

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login_view')
    return render(request, 'main/register.html')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
    return render(request, 'main/login.html')

from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        return redirect('login') 
    return render(request, 'main/register.html')

from django.shortcuts import render
from .models import Skill  

def skills_list(request):
    skills = Skill.objects.all()  
    return render(request, 'main/skills_list.html', {'skills': skills})

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request, f"Account created for {user.username}!")
            return redirect('homepage')  
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})

