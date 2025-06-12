from django.http import JsonResponse, HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from basketapp.models import Basket
from mainapp.models import Product
from mainapp.utils import get_main_menu


def basket(request):
    if request.user.is_authenticated:
        basket_ = Basket.objects.filter(user=request.user)
        context = {
            'basket': basket_,
            'menu_links': get_main_menu(),
        }
        return render(request, 'basketapp/basket.html', context)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_add(request, pk):
    product_ = get_object_or_404(Product, pk=pk)

    # ҚАТЕНІҢ АЛДЫН АЛАТЫН ҚАУІПСІЗ ТӘСІЛ:
    basket_, created = Basket.objects.get_or_create(user=request.user, product=product_)

    if not created:
        basket_.quantity += 1
    else:
        basket_.quantity = 1

    basket_.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk):
    basket_item = get_object_or_404(Basket, id=pk, user=request.user)
    basket_item.delete()
    return HttpResponseRedirect(reverse('basketapp:view'))
