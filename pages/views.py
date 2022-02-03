from django.shortcuts import render

# pages/views.py
from django.http import HttpResponse


def homePageView(request):
    return HttpResponse("<h2>Hello, World!</h2><p>We love <a href='https://code-crew.org'>CodeCrew<a/>!</p>")