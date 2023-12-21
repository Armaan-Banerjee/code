from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bookmarks = models.ManyToManyField("Bookmark", blank=True, related_name="Bookmark")

    def __str__(self):
        return f"{self.id} | {self.first_name} {self.last_name}"

class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    users = models.ManyToManyField("User", blank=True, related_name="Users")