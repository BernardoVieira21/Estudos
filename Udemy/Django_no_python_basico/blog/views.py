from django.shortcuts import render
from django.http import HttpResponse
from blog.data import posts

# Create your views here.

def blog(request):
    print('blog')

    context = {
        'text': 'Olá blog',
        'posts': posts
    }

    return render(request, 'blog/home.html', context)


def exemplo(request):
    print('exemplo')

    context = {
        'text': 'Olá exemplo',
        'title': 'Essa é uma página de exemplo',
    }

    return render(request, 'blog/exemplo.html', context)


def post(request, id):
    print('blog')

    context = {
        'text': 'Olá blog',
        'posts': posts
    }

    return render(request, 'blog/home.html', context)