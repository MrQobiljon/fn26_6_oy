from django.shortcuts import render

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

from .models import Category, Post


def home(request: WSGIRequest):
    posts = Post.objects.all()
    return render(request, 'index.html',
                  {"posts": posts})


def about(request: WSGIRequest):
    return HttpResponse("<h1>FN26 guruhi<h1>")


def contact(request):
    return HttpResponse("Contact")