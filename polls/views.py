from django.shortcuts import render
from django.http.response import HttpResponse

def index(request):
    om="Hello "
    context={
        "value":"this is om ",
        "cost":f"price less{om} ",
        "value":"this is om ",
        "value":"this is om ",
    }
    return render(request,"index.html",context)

def contact(request):
    return HttpResponse(f"This is Contact Page ")


def setting(request):
    return HttpResponse(f"This is setting page ")

