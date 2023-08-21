from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .models import Question

# Create your views here.
        
def index(request):
	latest_question_list = Question.objects.order_by("-pub_date")[:5]
	context = { "latest_question_list": latest_question_list}
	return render(request, "polls/index.html", context)	

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, "polls/detail.html", {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
		'question': question,
		'question_id': question_id,
	}
    return render(request, "polls/results.html", context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = { "question": question, "question_id" : question_id}
    return render(request, "polls/vote.html", context)
