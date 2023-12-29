from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Flashcard)
admin.site.register(Keyword)
admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(QuizAnswer)