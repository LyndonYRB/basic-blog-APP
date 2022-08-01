from django.shortcuts import render

from .models import BlogPost

# Create your views here.


def home(request):
    posts = BlogPost.objects.all()
    context = {'posts': posts}
    return render(request, 'home.html', context)
