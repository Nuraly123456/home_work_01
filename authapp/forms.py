from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from authapp.models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Пайдаланушы аты')
    password = forms.CharField(label='Құпиясөз', widget=forms.PasswordInput)


class ShopUserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.help_text = None

    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'email', 'age', 'avatar', 'password1', 'password2')

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError('Сен әлі 18-ге толмадың!')
        return age


class ShopUserEditForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.help_text = None
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'email', 'age', 'avatar', 'password')

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError('Сен әлі 18-ге толмадың!')
        return age
