from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Ankit',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': '14 March 2019'
    },
    {
        'author': 'itank',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': '15 March 2019'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
