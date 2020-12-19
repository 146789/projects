from django.urls import path
from . import views

urlpatterns = [
    path("", views.Blog_index, name="blog_index"),
    path("<int:pk>/", views.Blog_details, name="blog_details")

]
