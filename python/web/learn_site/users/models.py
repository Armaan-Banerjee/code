from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
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
    


class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("User", blank=True, null=True, on_delete=models.CASCADE)
    page = models.ForeignKey("info.Pages", on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def add_bookmark(self, name, user: User):
        new = Bookmark(name=name, user=user.id)
        new.save()

        return new
    
    def delete_bookmark(self):
        try:
            self.delete()
        except Exception as e:
            return e
        
    @staticmethod
    def query_all():
        all = Bookmark.objects.all()

        return all.values_list()

