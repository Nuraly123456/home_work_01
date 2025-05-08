# mainapp/views.py
from django.shortcuts import render
from .models import Product

def index(request):
    title = 'Главная страница'

    prods = Product.objects.all()[:3]

    context = {
        'title': title,
        'products': prods,
    }

    return render(request, 'index.html', context)

def contacts(request):
    return  render(request, 'contacts.html')

def about(request):
    return render(request, 'about.html')

def products(request):
    return render(request, 'products.html')

