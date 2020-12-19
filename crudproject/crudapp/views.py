from django.shortcuts import render, redirect
from crudapp.models import student
from crudapp.forms import StudentForm
from django.contrib import messages
from django.core.mail import send_mail
from crudproject import settings
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.


@login_required
def getStudents(request):
    students = student.objects.all()
    return render(request, 'crudapp/index.html', {'student': students})


@login_required
def createStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'crudapp/create.html', {'form': form})


@login_required
@permission_required('crudapp.delete_student')
def deleteStudent(request, id):
    students = student.objects.get(id=id)
    students.delete()
    return redirect('/')


@login_required
def updateStudent(request, id):
    students = student.objects.get(id=id)
    form = StudentForm(instance=students)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=students)
        if form.is_valid():
            form.save()
            messages.success(request, "updated successfully")
            return redirect('/')

    return render(request, 'crudapp/update.html', {'form': form})


def logout(request):
    return render(request, 'crudapp/logout.html')

# def sendmail(request):
#     if request.method == 'POST':
#         sd = request.POST['sdml']
#         sbj = request.POST['sb']
#         mssg = request.POST['mg']
#         df = settings.EMAIL_HOST_USER
#         t = send_mail(sbj, mssg, df, [sd])
#         if t == 1:
#             return redirect('/sendmail')
#     return render(request, 'crudapp/mail.html')
