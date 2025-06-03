from django.shortcuts import render

from mainapp.models import Product, Category


def get_main_menu(current='mainapp:index'):
    return [
        {'href': 'mainapp:index', 'name': 'Главная', 'active': current},
        {'href': 'mainapp:products', 'name': 'Товары', 'active': current},
        {'href': 'mainapp:about', 'name': 'О нас', 'active': current},
        {'href': 'mainapp:contacts', 'name': 'Контакты', 'active': current},
    ]


def index(request):
    title = 'Главная'

    prods = Product.objects.all()[:4]

    context = {
        'title': title,
        'products': prods,
        'menu_links': get_main_menu(),
    }

    return render(request, 'index.html', context)

def contacts(request):
    title = 'Контакты'
    context = {
        'title': title,
        'menu_links': get_main_menu('mainapp:contacts'),
    }
    return render(request, 'contacts.html', context)

def about(request):
    title = 'О нас'
    context = {
        'title': title,
        'menu_links': get_main_menu('mainapp:about'),
    }
    return render(request, 'about.html', context)

def products(request):
    title = 'Товары'
    prods = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'title': title,
        'products': prods,
        'categories': categories,
        'menu_links': get_main_menu('mainapp:products'),
    }
    return render(request, 'products.html', context)

def product(request, pk):
    title = 'Товар'

    prod = Product.objects.get(id=pk)
    same_prods = Product.objects.exclude(id=pk)

    context = {
        'title': title,
        'product': prod,
        'products': same_prods,
        'menu_links': get_main_menu('mainapp:products'),
    }
    return render(request, 'product.html', context)