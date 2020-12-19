from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def dispalyQuote(request):
    return HttpResponse("This is second django application")
