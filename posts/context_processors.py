from django.shortcuts import render

from .models import Post

def get_posts(request):
    return {'posts': Post.objects.all().order_by('-date')}