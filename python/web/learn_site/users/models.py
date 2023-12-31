from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.shortcuts import get_object_or_404
# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"{self.id} | {self.username}"
    
    def get_bookmarks(self):
        bookmarks = self.bookmark_set.all()
        return bookmarks
    
    def get_comments(self):
        comments = self.comment_set.all()
        return comments
    
    def get_flashcards(self):
        flashcards = self.flashcard_set.all()
        return flashcards


class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("User", blank=True, null=True, on_delete=models.CASCADE)
    page = models.ForeignKey("info.Pages", on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=255, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def add_bookmark( user: User, page, name=None):
        new = Bookmark(name=name, user=user, page=page)
        new.save()

        return new
    
    @staticmethod
    def check_if_valid(user, page):
        all = Bookmark.objects
    
    def delete_bookmark(self):
        try:
            self.delete()
        except Exception as e:
            return e
    
    @staticmethod
    def get_bookmark(user, page):
        bookmark = get_object_or_404(Bookmark, user=user, page=page)
        return bookmark
        
    @staticmethod
    def query_all():
        all = Bookmark.objects.all()

        return all.values_list()
    


