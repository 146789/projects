from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student
from django.urls import reverse_lazy
# Create your views here.


class studentListView(ListView):
    model = Student


class studentDetailView(DetailView):
    model = Student


class studentCreateView(CreateView):
    model = Student
    fields = ('firstName', 'lastName', 'Tscore')


class studentUpdateView(UpdateView):
    model = Student
    fields = ('Tscore',)


class studentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('stud')
