from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    return HttpResponse("<h1> Hello Django!</h1>")


def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1> Contact Page</h1>")


def about_view(request, *args, **kwargs):
    return HttpResponse("<h1> About page</h1>")
