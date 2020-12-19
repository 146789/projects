from django.shortcuts import render
from blogapp.models import Blog

# Create your views here.


def Blog_index(request):
    blog = Blog.objects.all()
    context = {
        'blog': blog
    }
    return render(request, 'blog_template/blog_index.html', context)


def Blog_details(request, pk):
    blog_detail = Blog.objects.get(pk=pk)
    context = {
        'blog_details': blog_detail
    }
    return render(request, 'blog_template/blog_details.html', context)
