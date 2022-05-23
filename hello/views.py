from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello Amdocs Team - Good Morning, How are you ? Today we are happy & we are learning Cloud Concepts")
