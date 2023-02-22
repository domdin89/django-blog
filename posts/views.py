from django.shortcuts import render

from categories.models import Category
from categories.views import category
from posts.models import Post


def home(request):
    post = Post.objects.all()
    cat = category(request)

    context = {
        'posts': post,
        'category': cat
    }
    return render(request, 'posts/home.html', context)

def blog(request):
    return render(request, 'posts/blog.html', category(request))

def post(request):
    return render(request, 'posts/post-details.html', category(request))