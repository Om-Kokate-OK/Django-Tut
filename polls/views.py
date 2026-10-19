from django.shortcuts import render
from django.http.response import HttpResponse

def index(request):
    return HttpResponse(f"This is my first response in poll app")
