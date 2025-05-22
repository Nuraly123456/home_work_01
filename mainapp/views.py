from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def index(request):
    products = Product.objects.all()[:3]
    return render(request, 'index.html', {
        'title': 'Главная страница',
        'products': products,
    })

def products(request):
    title = 'Товары'
    prods = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'products.html', {
        'title': title,
        'products': prods,
        'categories': categories
    })

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product.html', {
        'product': product,
        'title': product.name,
    })

def contacts(request):
    return render(request, 'contacts.html')

def about(request):
    return render(request, 'about.html')
