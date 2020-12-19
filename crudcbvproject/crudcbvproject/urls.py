"""crudcbvproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cbvcrudapp.views import studentListView, studentDetailView, studentCreateView, studentUpdateView, studentDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', studentListView.as_view(), name='stud'),
    path('<int:pk>/', studentDetailView.as_view(), name='detail'),
    path('create/', studentCreateView.as_view()),
    path('update/<int:pk>/', studentUpdateView.as_view()),
    path('delete/<int:pk>/', studentDeleteView.as_view())
]
