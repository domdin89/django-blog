from django.shortcuts import render, redirect
from django.contrib import messages

from posts.forms import NewPostForm
from posts.models import Post



def blog(request):
    return render(request, 'posts/blog.html')

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'posts/post-details.html', {'post': post})

def new(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = NewPostForm()
    return render(request, 'posts/add_post.html', {'form': form})