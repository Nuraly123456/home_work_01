from django.shortcuts import render, get_object_or_404

from mainapp.models import Product, Category

from basketapp.models import Basket

from mainapp.utils import get_main_menu, get_basket


def index(request):
    title = 'Басты бет'

    prods = Product.objects.all()[:4]

    basket = []

    if request.user.is_authenticated:
        basket = get_basket(request.user)


    context = {
        'title': title,
        'products': prods,
        'menu_links': get_main_menu(),
        'basket': basket,
    }

    return render(request, 'index.html', context)

def contacts(request):
    title = 'Хабарласу'

    if request.user.is_authenticated:
        basket = get_basket(request.user)

    context = {
        'title': title,
        'menu_links': get_main_menu('mainapp:contacts'),
        'basket': basket,
    }
    return render(request, 'contacts.html', context)

def about(request):
    title = 'Біз туралы'

    if request.user.is_authenticated:
        basket = get_basket(request.user)

    context = {
        'title': title,
        'menu_links': get_main_menu('mainapp:about'),
        'basket': basket,
    }
    return render(request, 'about.html', context)

def products(request, pk=None):
    title = 'Өнімдер'
    prods = Product.objects.all()
    categories = Category.objects.all()

    basket = []

    if request.user.is_authenticated:
        basket = get_basket(request.user)

    context = {
        'title': title,
        'products': prods,
        'categories': categories,
        'menu_links': get_main_menu('mainapp:products'),
        'basket': basket,
    }

    if pk is not None:
        if pk == 0:
            products_ = Product.objects.all()
            category = {'name': 'барлығы'}
        else:
            category = get_object_or_404(Category, pk=pk)
            products_ = Product.objects.filter(category__pk=pk)

        context.update({'products': products_, 'category': category})


    return render(request, 'products.html', context)

def product(request, pk):
    title = 'Өнім'

    prod = Product.objects.get(id=pk)
    same_prods = Product.objects.exclude(id=pk)


    if request.user.is_authenticated:
        basket = get_basket(request.user)

    context = {
        'title': title,
        'product': prod,
        'products': same_prods,
        'menu_links': get_main_menu('mainapp:products'),
        'basket': basket,
    }
    return render(request, 'product.html', context)