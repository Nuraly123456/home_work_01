from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product



def basket(request):
    if request.user.is_authenticated:
        basket_ = Basket.objects.filter(user=request.user)
        context = {
            'basket': basket_,
        }
        return render(request, 'basketapp/basket.html', context)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_add(request, product_id):
    product_ = get_object_or_404(Product, id=product_id)

    # Try to get existing basket item or create a new one
    basket_item, created = Basket.objects.get_or_create(
        user=request.user,
        product=product_,
        defaults={'quantity': 1}
    )

    if not created:
        basket_item.quantity += 1
        basket_item.save()

    return JsonResponse({'status': 'success'})
def basket_remove(request, pk):
    return render(request, 'basketapp/basket.html')