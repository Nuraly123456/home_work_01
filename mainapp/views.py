from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()[:3]
    return render(request, 'index.html', {'title': 'Главная страница', 'products': products})

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'title': 'Products', 'products': products})

def contacts(request):
    return render(request, 'contacts.html')

def about(request):
    return render(request, 'about.html')
