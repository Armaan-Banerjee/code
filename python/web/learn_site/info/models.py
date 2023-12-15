from django.db import models
import uuid
from django.utils import timezone

# Create your models here.

class page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    data = models.TextField()
    tags = models.ManyToManyField("Tags", blank=True, related_name="pages")

    def __str__(self):
        return f"{self.title} | {self.id}"
    
    def add_page(self, title, data):
        new_page = page(title=title, data=data)
        new_page.save()

        return new_page.id
    
    def show_tags(self):
        return self.tags.all()
    
    def add_tag(self, tag_id):

        try:
            tag = Tags.objects.get(id=tag_id)
            self.tags.add(tag)
            self.save()
            return 1
        
        except:
            return -1


    def delete_tag(self, tag_id):
        try:
            tag = Tags.objects.get(id=tag_id)
            self.tags.remove(tag)
            self.save()

            return 1
        except:
            return -1
    
class Tags(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    pages = models.ManyToManyField("page", blank=True, related_name="tags")
    details = models.CharField(null=True, blank=True, default="")
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = True

    def update_name(self, name):
        self.name = name
        self.save()

        return self.name

    def delete_tag(self):
        try:
            pages = self.pages

            for page in pages:
                page.tags.remove(self)

            self.delete()

            return 1
        
        except:
            return -1


    @staticmethod
    def check_if_valid(name):
        results = Tags.objects.filter(name=name)
        if len(results) > 0:
            return False
        else:
            return True
        
    def list_all():
        results = Tags.objects.all().values_list("name", flat=True)
        return results
    
    def set_all():
        results = Tags.objects.all().values()
        end = []
        for res in results:
            ou = (res["id"], res["name"])
            end.append(ou)

        return end
    
    def show_pages(self):
        return self.pages.all()
    
    def __str__(self):
        return f"{self.name}"


