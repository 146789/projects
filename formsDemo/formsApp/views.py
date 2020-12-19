from django.shortcuts import render
from . import forms
# Create your views here.


def userRegistrationView(request):
    form = forms.UserRegistrationform()
    if request.method == 'POST':
        form = forms.UserRegistrationform(request.POST)
        if form.is_valid():
            print("form is valid")
            print("firstName is ", form.cleaned_data['firstName'])
            print('lastName is ', form.cleaned_data['lastName'])
            print('email is ', form.cleaned_data['email'])
    return render(request, "formsDemo/userRegistration.html", {'form': form})
