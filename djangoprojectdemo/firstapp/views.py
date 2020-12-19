from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


def display(request):
    return HttpResponse("<h1>hello django</h1>")


def displayTime(request):
    dt = datetime.datetime.now()
    s = "<b>Current datetime </b>" + str(dt)
    return HttpResponse(s)
