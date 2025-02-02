from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from .forms import ContactForm


# Create your views here.

def home(request):
    form = ContactForm()
    return render(request, 'portafolio/home.html', {'form': form, 'welcome_message': _("Welcome to my website!"),  })

def about_me(request):
    return render(request, 'portafolio/about_me.html',{'title': _("About Me"), 'description': _("Here you will find more information about me.")})

def studies(request):
    return render(request, 'portafolio/studies.html', {'title': _("Studies"), 'description': _("These are my academic studies.")}  )

def experience(request):
    return render(request, 'portafolio/experience.html', {'title': _("Experience"), 'description': _("Here you will find my professional experiences.")})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return render(request, 'portafolio/home.html', {'form': ContactForm(), 'show_modal': True})
    else:
        form = ContactForm()
    return render(request, 'portafolio/home.html', {'form': form, 'title': _("Contact"), 'message_sent': _("Your message has been sent successfully!")  })