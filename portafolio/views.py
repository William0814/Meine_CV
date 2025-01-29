from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'portafolio/home.html', {'form': form})

# Create your views here.

def home(request):
    form = ContactForm()
    return render(request, 'portafolio/home.html', {'form': form})

def about_me(request):
    return render(request, 'portafolio/about_me.html')

def studies(request):
    return render(request, 'portafolio/studies.html')

def experience(request):
    return render(request, 'portafolio/experience.html')
