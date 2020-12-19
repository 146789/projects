from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Student
# Create your views here.


# class GreetView(View):
#     greetMessage = "<h1>Hello class based view</h1>"

#     def get(self, request):
#         return HttpResponse(self.greetMessage)

class studentListView(ListView):
    model = Student
