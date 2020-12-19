from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def indexpage(request):
    return HttpResponse("welcome to django")


def printName(request, name):
    return render(request, "demo/name.html", {'name': name})


def RollnUmber(request, name, rollnumber):
    mydict = {"name": name, 'rollnumber': rollnumber}
    return render(request, 'demo/demo2.html', mydict)


def rcrd(request, name, age, email):
    return HttpResponse(f"name : <h2>{name}</h2> age :  <h3>{age}</h3>  email : <h4>{email}</h4>")


def altr(request, name, age):
    return HttpResponse(f"<script>alert('the name is {name}')</script><h2> hello {name}</h2><h2>your are {age} years old</h2>")


def sample(request):
    return render(request, 'demo/index.html')
