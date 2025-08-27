from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta para la página de inicio
    path('about', views.about, name='about'),  # Ruta para la página "Acerca de"
    path('services', views.services, name='services'),  # Ruta para la página de servicios
    path('contact', views.contact, name='contact'),  # Ruta para la página de contacto
]

