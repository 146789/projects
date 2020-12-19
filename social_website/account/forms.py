from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


# class UserRegistrationForm(forms.ModelForm):
#     password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
#         attrs={"class": "form-control", "placeholder": "Enter password", "required": True}))
#     password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(
#         attrs={"class": "form-control", "placeholder": "Enter password again", "required": True}))

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email')
#         widgets = {
#             'username': forms.TextInput(attrs={
#                 "class": "form-control",
#                 "placeholder": "Enter username",
#                 "required": True
#             }),
#             'first_name': forms.TextInput(attrs={
#                 "class": "form-control",
#                 "placeholder": "Enter your first name",
#                 "required": True
#             }),
#             "last_name": forms.TextInput(attrs={
#                 "class": "form-control",
#                 "placeholder": "Enter your last name",
#                 "required": True
#             }),
#             'email': forms.EmailInput(attrs={
#                 "class": "form-control",
#                 "placeholder": "Enter email address",
#                 "required": True
#             })
#         }

#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password1'] != cd['password2']:
#             raise forms.ValidationError('password does not match')
#         return cd['password2']


# class UserEditForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')


# class ProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = Profiles
#         fields = ('date_of_birth', 'Photo')

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
