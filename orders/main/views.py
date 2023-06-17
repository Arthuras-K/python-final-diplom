from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h4>Hello</h4>")

def start(request):
    return render("<h2>start</h2>")