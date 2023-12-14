from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from ..models import  Tag
from ..forms import  create_new_tag

def add_new_tag(request):
    if request.method == "POST":
        form = create_new_tag(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            name = form.cleaned_data["name"]

            if not Tag.check_if_valid(name=name):
                return HttpResponse("Error: tag already exists")
            
            new_tag = Tag(name=name)
            new_tag.save()

            return HttpResponseRedirect("/")

def show_tag_details(request, name, id):
    tag = Tag.objects.get(id=id)

    pages = tag.pages.all()

    


