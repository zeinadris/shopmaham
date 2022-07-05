from urllib import request
from django.shortcuts import render

def welcome(request):
    return render(request, 'base.html')