from django.db import models
import uuid

# Create your models here.

class Flashcard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    private = models.BooleanField(default=True)
    user = models.ForeignKey("users.User", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} | {self.title}"

    @staticmethod
    def all_public():
        return Flashcard.objects.filter(private=False)
    
    def all_cards(self):
        return self.keyword_set.all()

class Keyword(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    front = models.TextField()
    back  = models.TextField()
    flashcard = models.ForeignKey("Flashcard", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} | {self.front}"

class Quiz(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)

    def all_questions(self):
        return self.quizquestion_set.all()
    
    def full_quiz(self):
        outdict = {}
        questions = self.all_questions()
        for question in questions:
            answers = question.all_answers()
            
            answerdict = {}
            for ans in answers:
                answerdict[str(ans.id)] = ans.answer
            
            outdict[str(question.id)] = [question.question, answerdict]
        
        return outdict


class QuizQuestion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.TextField()
    quiz = models.ForeignKey("Quiz", blank=True, null=True, on_delete=models.CASCADE)

    def all_answers(self):
        return self.quizanswer_set.all()

class QuizAnswer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    answer = models.TextField()
    question = models.ForeignKey("QuizQuestion", blank=True, null=True, on_delete=models.CASCADE)