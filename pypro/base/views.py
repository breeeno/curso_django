from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(requests):
    return HttpResponse('Olá Django!')