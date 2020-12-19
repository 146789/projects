from django.shortcuts import render
from DemoApp5.form import Usrgt, usUp
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'DemoApp5/home.html')


def about(request):
    return render(request, 'DemoApp5/about.html')


def usrg(request):
    if request.method == "POST":
        t = Usrgt(request.POST)
        if t.is_valid():
            t.save()
            messages.success(request, "user registered successfully")

    t = Usrgt()
    return render(request, 'DemoApp5/register.html', {'y': t})


@login_required
def db(request):
    return render(request, 'DemoApp5/dash.html')


@login_required
def profile(request):
    return render(request, 'DemoApp5/profile.html')


@login_required
def updated(request):
    q = usUp()
    return render(request, "DemoApp5/update.html", {'u': q})
