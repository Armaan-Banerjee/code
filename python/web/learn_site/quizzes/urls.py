from django.urls import path
from .views.quiz import api_quizzes
from .views.flashcard import flashcard_view, all_flashcards_view, add_flashcard_view

urlpatterns = [
    path("quizzes/api/all", api_quizzes, name="api_quizzes"),
    path("flashcard/<uuid:id>/<str:title>", flashcard_view, name="flashcard_view"),
    path("flashcards/all", all_flashcards_view, name="all flashcards"),
    path("flashcards/add", add_flashcard_view, name="add flashcard")
]