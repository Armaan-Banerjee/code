from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from ..models import Flashcard, Keyword, Quiz, QuizQuestion, QuizAnswer

# Create your views here.

def api_quizzes(request):
    quizlist = []
    
    quizzes = Quiz.objects.all()
    for quiz in quizzes:
        quizdict = {str(quiz.id): [quiz.title, quiz.full_quiz()]}
        quizlist.append(quizdict)
    
    outdict = {"quizzes": quizlist}

    return JsonResponse(outdict)