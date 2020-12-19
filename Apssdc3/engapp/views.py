from django.shortcuts import render, redirect
from engapp.models import Register
from django.http import HttpResponse
# Create your views here.
from engapp.forms import regform


def register(request):
    if request.method == "POST":
        c = request.POST['cname']
        n = request.POST['name']
        r = request.POST['roll']
        b = request.POST['branch']
        y = request.POST['year']
        Register.objects.create(collageaname=c, name=n,
                                roll=r, branch=b, year=int(y))
        return redirect('/display')

    return render(request, 'engapp/register.html')


def display(request):
    data = Register.objects.all()
    return render(request, 'engapp/display.html', {'data': data})


def delete(request, id):
    data = Register.objects.get(id=id)
    data.delete()
    return redirect('/display')


def update(request, name):
    data = Register.objects.get(name=name)
    if request.method == "POST":
        c = request.POST['cname']
        n = request.POST['name']
        r = request.POST['roll']
        b = request.POST['branch']
        y = request.POST['year']
        data.collageaname = c
        data.name = n
        data.roll = r
        data.branch = b
        data.year = y
        data.save()
        return redirect('/display')
    return render(request, 'engapp/update.html', {'data': data})


def userreg(request):
    form = regform()

    if request.method == 'POST':
        form = regform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'engapp/show.html')
    return render(request, 'engapp/userreg.html', {'form': form})

def Show(request):
    