from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'portafolio/home.html')

def about_me(request):
    return render(request, 'portafolio/about_me.html')

def studies(request):
    return render(request, 'portafolio/studies.html')

def experience(request):
    return render(request, 'portafolio/experience.html')
