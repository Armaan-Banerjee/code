from django.contrib import admin
from .models import Pages, Tags, Comment
# Register your models here.

admin.site.register(Pages)
admin.site.register(Tags)
admin.site.register(Comment)