from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Service
from .forms import ContactForm
from django.contrib import messages
from .models import ContactMessage

# views
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def skills(request):
    return render(request, 'skills.html')

def resume(request):
    return render(request, 'resume.html')

def services(request):
    return render(request, 'services.html')
def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save to the database
        ContactMessage.objects.create(name=name, email=email, message=message)

        # Show success message
        messages.success(request, "Your message has been sent successfully!")
        return redirect("contact")  # Redirect to prevent form resubmission

    return render(request, "contact.html")