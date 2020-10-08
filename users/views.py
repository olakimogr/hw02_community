from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("login") # где login - это параметр "name" в path()
    template_name = "signup.html"


import datetime as dt


def year(request):
    """
    Добавляет переменную с текущим годом.
    """
    return {
        "year": dt.datetime.now().year
    }