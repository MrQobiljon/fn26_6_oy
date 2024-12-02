from django.shortcuts import render

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

from .models import Category, Post


def home(request: WSGIRequest):
    posts = Post.objects.all()
    categories = Category.objects.all()

    context = {
        "posts": posts,
        "categories": categories
    }

    return render(request, 'index.html', context)


def about(request: WSGIRequest):
    return render(request, 'about.html')


def contact(request):
    return HttpResponse("Contact")