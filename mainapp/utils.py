from basketapp.models import Basket

def get_main_menu(current='mainapp:index'):
    return [
        {'href': 'mainapp:index', 'name': 'Басты бет', 'active': current},
        {'href': 'mainapp:products', 'name': 'Өнімдер', 'active': current},
        {'href': 'mainapp:about', 'name': 'Біз туралы', 'active': current},
        {'href': 'mainapp:contacts', 'name': 'Хабарласу', 'active': current},
    ]
def get_basket(user=None):
    if user:
        return Basket.objects.filter(user=user)
    return None