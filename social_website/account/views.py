from django.shortcuts import render
#from account.forms import Loginform
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .models import Profile
from .forms import UserRegistrationForm, \
    UserEditForm, ProfileEditForm
from django.contrib import messages

# Create your views here.


# def user_login(request):
#     if request.method == 'POST':
#         form = Loginform(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(
#                 request, username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated')
#                 else:
#                     return HttpResponse('Disabled')
#             else:
#                 return HttpResponse('invalid login')
#     else:
#         form = Loginform()
#     return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


# def Register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             # create a new user object but avoid saving it yet
#             new_user = user_form.save(commit=False)
#             # set choosen password
#             new_user.set_password(user_form.cleaned_data['password1'])
#             # save the user object
#             new_user.save()
#             Profiles.objects.create(user=new_user)
#             return render(request, 'account/register_done.html', {'new_user': new_user})

#     else:
#         user_form = UserRegistrationForm()
#     return render(request, 'account/register.html', {'user_form': user_form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)

            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})


# @login_required
# def edit(request):
#     if request.method == 'POST':
#         user_form = UserEditForm(instance=request.user, data=request.POST)
#         Profile_form = ProfileEditForm(
#             instance=request.user.profiles, data=request.POST, files=request.FILES)

#         if user_form.is_valid() and Profile_form.is_valid():
#             user_form.save()
#             Profile_form.save()
#     else:

#         user_form = UserEditForm(instance=request.user)
#         Profile_form = ProfileEditForm(instance=request.user.profiles)

#     return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': Profile_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'profile updated successfully')
        else:
            messages.error(request, 'Error in updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
            instance=request.user.profile)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})
