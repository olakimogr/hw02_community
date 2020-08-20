import datetime as dt

from django.shortcuts import get_object_or_404, render

from .models import Group, Post



def index(request):
    latest = Post.objects.all()[:11]
    return render(request, 'index.html', {'posts': latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    return render(request, 'group.html', {'group': group, 'posts': posts})


def year(request):
    date = dt.datetime.now().year
    return { 'year' : date }
