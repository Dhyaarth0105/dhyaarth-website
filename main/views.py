from django.shortcuts import render, redirect
from .models import ContactMessage
from django.contrib import messages

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def industries(request):
    return render(request, 'main/industries.html')

def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            full_name=full_name,
            email=email,
            message=message
        )

        messages.success(request, "Thank you! Your message has been received.")
        return redirect('contact')  # or wherever you want

    return render(request, 'main/contact.html')

def portfolio(request):
    return render(request, 'main/portfolio.html')

def testimonials(request):
    return render(request, 'main/testimonials.html')

def blog(request):
    return render(request, 'main/blog.html')

# --- New Views for Services Subpages ---
def python_automation(request):
    return render(request, 'main/services/python_automation.html')

def rpa(request):
    return render(request, 'main/services/rpa.html')

def intelligent_document_processing(request):
    return render(request, 'main/services/intelligent_document_processing.html')

def chatbot(request):
    return render(request, 'main/services/chatbot.html')

# --- New Views for Industries Subpages ---
def manufacturing(request):
    return render(request, 'main/industries/manufacturing.html')

def healthcare(request):
    return render(request, 'main/industries/healthcare.html')

def finance(request):
    return render(request, 'main/industries/finance.html')

def retail(request):
    return render(request, 'main/industries/retail.html')

