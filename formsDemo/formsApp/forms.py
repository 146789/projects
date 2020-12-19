from django import forms
from django.core import validators


class UserRegistrationform(forms.Form):
    GEN = [('male', 'MALE'), ('female', 'FEMALE')]
    firstName = forms.CharField(required=False, validators=[
                                validators.MinLengthValidator(5), validators.MaxLengthValidator(20)])
    lastName = forms.CharField()
    email = forms.CharField()
    gender = forms.CharField(widget=forms.Select(choices=GEN))
    password = forms.CharField(widget=forms.PasswordInput)

    # def clean(self):
    #     user_cleaned_data = super().clean()
    #     fn = user_cleaned_data['firstName']
    #     if len(fn) > 20:
    #         raise forms.ValidationError(
    #             "The length of first name should not be greater than 20 characters")
    #     em = user_cleaned_data['email']
    #     if em.find('@') == -1:
    #

    #         raise forms.ValidationError("The email should have @ symbol")
    # def clean_firstName(self):
    #     fn = self.cleaned_data['firstName']
    #     if len(fn) > 20:
    #         raise forms.ValidationError(
    #             "The max length of first name is 20 characters")
    #     return fn

    # def clean_email(self):
    #     em = self.cleaned_data['email']
    #     if em.find('@') == -1:
    #         raise forms.ValidationError(
    #             "The email should contain @ symbol check ")
    #     return em
