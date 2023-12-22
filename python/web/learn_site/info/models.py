from django.db import models
import uuid
from django.utils import timezone

# Create your models here.
class Tags(models.Model):

    class Meta:
        db_table = 'info_tags'
        managed = True

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    pages = models.ManyToManyField("Pages", blank=True, related_name="Tags")
    details = models.TextField(null=True, blank=True, default="")
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = ("Tags")

    def add_tag(self, name, details="", pages_optional="", *args, **kwargs):
        new = Tags(name=name, details=details)
        new.save()

        if pages_optional != "":
            new.pages.add(pages_optional)

    def add_pages(self, pages: list):
        for page in pages:
            self.Tags.add(page)
        
        return self.Pages

    def delete_pages(self, pages: list):
        for page in pages:
            self.Pages.remove(page)

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
        results = Tags.objects.filter(name=name).exists()
        return results
        
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


class Pages(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    data = models.TextField()
    tags = models.ManyToManyField("Tags", blank=True, related_name="Pages")

    class Meta:
        verbose_name_plural = ("Pages")

    def __str__(self):
        return f"{self.title} | {self.id}"
    
    def add_page(self, title, data):
        new_page = Pages(title=title, data=data)
        new_page.save()

        return new_page.id
    
    def show_tags(self):
        return self.Tags.all()
    
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
    
    def add_comment(self, text, user):
        comment = Comment(text=text, user=user.id, page=self.id)
    
class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    pages = models.ForeignKey("Pages", blank=True, null=True ,on_delete=models.SET_NULL)
    user = models.ForeignKey("users.User", on_delete=models.SET_NULL, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return f"{self.id} | {self.text}"

    @staticmethod
    def add_comment( text: str, user, page: Pages):
        new_comment = Comment(text=text, user=user, pages=page)
        new_comment.save()

        return new_comment


    