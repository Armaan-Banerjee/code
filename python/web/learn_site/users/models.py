from django.utils import timezone
from django.db import models
import uuid
import datetime
# Create your models here.

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    backup_email = models.EmailField(null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    bookmarks = models.ManyToManyField("Bookmark", blank=True, related_name="Bookmark")

    def __str__(self):
        return f"{self.id} | {self.first_name} {self.last_name}"

class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    users = models.ManyToManyField("User", blank=True, related_name="Users")