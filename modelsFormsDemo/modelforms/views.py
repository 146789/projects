from django.shortcuts import render
from modelforms.forms import projectForm
from modelforms.models import Project
# Create your views here.


def index(request):
    return render(request, 'modelforms/index.html')


def listProjects(request):
    projectlist = Project.objects.all()
    return render(request, 'modelforms/listProjects.html', {'projects': projectlist})


def addProject(request):
    form = projectForm
    if request.method == 'POST':
        form = projectForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request, 'modelforms/addproject.html', {'form': form})
