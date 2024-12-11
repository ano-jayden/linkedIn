from django.shortcuts import render

def home(request):
    return render(request, 'personal/home.html')

def page1(request):
    return render(request, 'personal/page1.html')

def page2(request):
    return render(request, 'personal/page2.html')
