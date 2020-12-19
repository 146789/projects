from django.shortcuts import render
from posts.models import Post, Comment
from .forms import CommentForm
# Create your views here.


def blog_post(request):
    post1 = Post.objects.all().order_by('-created_on')
    context = {
        'post1': post1
    }
    return render(request, "posts/blog_post.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category).order_by('-created_on')
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'posts/blog_category.html', context)


def blog_details(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form
    }
    return render(request, "posts/blog_d.html", context)


def dashboard(request):
    return render(request, 'users/dashboard.html')
