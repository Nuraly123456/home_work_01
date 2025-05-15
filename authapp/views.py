from django.contrib import auth
from django.shortcuts import render, redirect
from authapp.forms import ShopUserLoginForm
from django.urls import reverse
from django.http import HttpResponseRedirect

def login(request):
    title = 'Кіру'

    if request.method == 'POST':
        login_form = ShopUserLoginForm(data=request.POST)

        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        login_form = ShopUserLoginForm()

    context = {
        'title': title,
        'login_form': login_form,
    }

    return render(request, 'auth/login.html', context)

def logout(request):
    auth.logout(request)
    return redirect(reverse('mainapp:index'))

def register(request):
    title = 'Тыркелу'

    context = {
        'title': title,
    }

    return render(request, 'auth/register.html', context)