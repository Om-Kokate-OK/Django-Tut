from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http.response import HttpResponse 
from django.http import Http404
from .models import Question


def details(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def result(request,question_id):
    return HttpResponse(f"You are looking ar question answer{question_id}")

def vote(request,question_id):
    return HttpResponse(f"Your are voting question no {question_id}")


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5] 
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context,request))

def contact(request):
    return HttpResponse(f"This is Contact Page ")


def setting(request):
    return HttpResponse(f"This is setting page ")

