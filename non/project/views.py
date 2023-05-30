from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home (request):
    return HttpResponse("Welcome  to django")

def shop (request):
    return HttpResponse("Welcome  to shop")
def about (request):
    return HttpResponse("Welcome  to about")
def blog (request):
    return HttpResponse("Welcome  to blog page")
def gallery (request):
    return HttpResponse("Welcome  to gallery")    