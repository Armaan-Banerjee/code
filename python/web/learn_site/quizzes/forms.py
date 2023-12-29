from django import forms 
from .models import Flashcard

class CreateFlashCard(forms.Form):
    title = forms.CharField(max_length=255)
    user_id = forms.UUIDField
    