from django.contrib import admin
from mainapp.models import Category, Product  # ЕКІ моделді де импорттау керек

admin.site.register(Category)
admin.site.register(Product)
