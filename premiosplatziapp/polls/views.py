from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Esto va ser epico papus")

