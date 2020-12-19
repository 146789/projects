from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'Demo2/home.html')


def about(request):
    return render(request, 'Demo2/about.html')
