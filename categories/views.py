from django.shortcuts import render

from categories.models import Category


def category(request):
    category = Category.objects.all()

    return {'category': category}


def detail_category(request, id):
    category = Category.objects.get(id=id)

    return {'category_det': category}