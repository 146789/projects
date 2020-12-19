from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_post, name="blog_post"),
    path('<int:pk>/', views.blog_details, name="blog_details"),
    path('<category>/', views.blog_category, name="blog_category"),
    path('dashboard/', views.dashboard, name="dash")
]
