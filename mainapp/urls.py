from django.urls import path

from mainapp.views import index, contacts, about

app_name ='mainapp'

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about'),
    path('products/', about, name='products'),
    path('product/', about, name='product'),
]