from django.db import models
import uuid

# Create your models here.

class page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    data = models.TextField()
    tags = models.ManyToManyField("Tag", blank=True, related_name="page")

    def __str__(self):
        return f"{self.title} | {self.id}"
    
    def add_page(self, title, data):
        new_page = page(title=title, data=data)
        new_page.save()

        return new_page.id
    
    def show_tags(self):
        return self.tags
    
class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    pages = models.ManyToManyField("page", blank=True, related_name="tag")

    @staticmethod
    def check_if_valid(name):
        results = Tag.objects.filter(name=name)
        if len(results) > 0:
            return False
        else:
            return True
        
    def list_all():
        results = Tag.objects.all().values_list("name", flat=True)
        return results
    
    def set_all():
        results = Tag.objects.all().values()
        end = []
        for res in results:
            ou = (res["id"], res["name"])
            end.append(ou)

        return end
    
    def __str__(self):
        return f"{self.name}"
