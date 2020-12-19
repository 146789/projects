from django.shortcuts import render

# Create your views here.


def renderTemplate(request):
    mydict = {"name": "naveen"}
    return render(request, 'templatesApp/firsttemplate.html', context=mydict)


def renderEmployee(request):
    mydict1 = {"id": 123, "name": "naveen", "salary": 10000}
    return render(request, 'templatesApp/Employee.html', mydict1)
