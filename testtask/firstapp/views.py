from django.shortcuts import render
from django.http import HttpResponse
from random import randint as rnd

def index(request):
    value = rnd(1000,10000)
    return HttpResponse(f'{value}')
