from django.shortcuts import render, get_object_or_404

from .models import Group, Post


def index(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    #не смог найти в документации ничего применимого к фильтрации полей при создании модели
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by("-pub_date")[:12]
    return render(request, "group.html", {"group": group, "posts": posts})

#не смог добиться взаимности от related_name.
#конструкция posts = Post.objects.select_related('group').all() выводит все посты всех групп.
