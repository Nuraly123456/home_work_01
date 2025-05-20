from django.contrib import auth
from django.shortcuts import render, redirect
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
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

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()


    context = {
        'title': title,
        'register_form': register_form,
    }

    return render(request, 'auth/register.html', context)



def edit(request):
    title = 'Озгерту не тузету'

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm()


    context = {
        'title': title,
        'edit_form': edit_form,
    }

    return render(request, 'auth/edit.html', context)