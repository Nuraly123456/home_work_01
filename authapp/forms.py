from django.contrib.auth.forms import AuthenticationForm
from django import forms
from authapp.models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    def clean_age(self):
        data = self.cleaned_data['age']

        if data < 18:
            raise forms.ValidationError('Сен алы  жассын !')
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name',
                  'password1', 'password2',
                  'email', 'age', 'avatar')