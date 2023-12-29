from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from ..models import Flashcard, Keyword, Quiz, QuizQuestion, QuizAnswer

# Create your views here.

def add_flashcard(request):
    flashcard = ""


def flashcard_view(request, id, title):
    flashcard = get_object_or_404(Flashcard, id=id)
    
    if flashcard.private:
        current_user = request.user
        if not current_user.is_authenticated:
            return HttpResponse("No can do")
        if current_user != flashcard.user.id:
            return HttpResponse("you are not allowed ")
    
    template = loader.get_template("flashcard.html")
    
    context = {
        "flashcard": flashcard,
        "keywords": flashcard.all_cards(),
        "user": flashcard.user
    }

    return HttpResponse(template.render(context, request))

def all_flashcards_view(request):
    flashcards = Flashcard.all_public()

    template = loader.get_template("allflashcards.html")

    context = {
        "flashcards": flashcards
    }

    return HttpResponse(template.render(context, request))

