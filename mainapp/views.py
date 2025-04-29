# mainapp/views.py
from django.shortcuts import render

def index(request):
    title = 'Главная страница'

    context = {
        'title': title,
    }

    return render(request, 'index.html', context)

def contacts(request):
    return  render(request, 'contacts.html')

def about(request):
    return render(request, 'about.html')

def products(request):
    return render(request, 'products.html')

def product(request):
    return render(request, 'product.html')

def base(request):
    return render(request, 'base.html')