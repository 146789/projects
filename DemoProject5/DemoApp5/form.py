
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class Usrgt(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Enter password", "required": True}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Enter password again", "required": True}))

    class Meta:
        model = User
        fields = ['username', 'email', ]
        widgets = {
            'username': forms.TextInput(attrs={
                "class": 'form-control',
                "placeholder": "Enter your username",
                "required": True

            }),
            'email': forms.TextInput(attrs={
                "class": "form-control",
                'placeholder': 'Enter your email',
                "required": True
            })
        }


class usUp(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                "class": 'form-control',

            }),
            'first_name': forms.TextInput(attrs={
                "class": 'form-control',
                'placeholder': "update first name"

            }),
            'last_name': forms.TextInput(attrs={
                "class": 'form-control',
                'placeholder': "update last name"

            }),
            

            'email': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "update email"
            })
        }
