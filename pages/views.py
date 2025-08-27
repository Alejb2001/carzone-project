from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')  # Renderiza la plantilla 'home.html'

def about(request):
    return render(request, 'pages/about.html')  # Renderiza la plantilla 'about.html'

def services(request):
    return render(request, 'pages/services.html')  # Renderiza la plantilla 'services.html'

def contact(request):
    return render(request, 'pages/contact.html')  # Renderiza la plantilla 'contact.html'