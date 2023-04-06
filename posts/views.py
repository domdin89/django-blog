from django.shortcuts import render

from posts.models import Post



def blog(request):
    return render(request, 'posts/blog.html')

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'posts/post-details.html', {'post': post})
