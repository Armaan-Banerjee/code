from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from ..models import  Tags
from ..forms import  create_new_tag, edit_tag

def add_new_tag(request):
    if request.method == "POST":
        form = create_new_tag(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            details = form.cleaned_data["details"]

            if Tags.check_if_valid(name=name):
                return HttpResponse("Error: tag already exists")
            
            if details != "":
                new_tag = Tags(name=name, details=details)
                new_tag.save()
            else:
                new_tag = Tags(name=name)
                new_tag.save()

            return HttpResponseRedirect("/page/add")
    else:
        return HttpResponse("na")

def show_tag_details(request, name, id):
    tag = Tags.objects.get(id=id)

    pages = tag.pages.all()

    template = loader.get_template("tag_page.html")

    context = {
        "tag" : tag,
        "pages" : pages
    }

    return HttpResponse(template.render(context, request))

def edit_tag(request, name, id):
    tag = Tags.objects.get(id=id)

    if request.method == "POST":
        form = edit_tag(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            details = form.cleaned_data["details"]

            if Tags.check_if_valid(name=name):
                return HttpResponse("Error: tag already exists")
            
            if details != "":
                tag.details = details
                tag.name = name
                tag.save()
            else:
                tag.name = name
                tag.save()

def tag_glossary(request):
    tags = Tags.objects.all()

    template = loader.get_template("tag_glossary.html")

    context = {
        "tags" : tags
    }

    return HttpResponse(template.render(context, request))







