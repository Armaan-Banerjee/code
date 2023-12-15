from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from ..models import  Tags
from ..forms import  create_new_tag

def add_new_tag(request):
    if request.method == "POST":
        form = create_new_tag(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            name = form.cleaned_data["name"]

            if not Tags.check_if_valid(name=name):
                return HttpResponse("Error: tag already exists")
            
            new_tag = Tags(name=name)
            new_tag.save()

            return HttpResponseRedirect("/")

def show_tag_details(request, name, id):
    tag = Tags.objects.get(id=id)

    pages = tag.pages.all()

    template = loader.get_template("tag_page.html")

    context = {
        "tag" : tag,
        "pages" : pages
    }

    return HttpResponse(template.render(context, request))

def tag_glossary(request):
    tags = Tags.objects.all()

    template = loader.get_template("tag_glossary.html")

    context = {
        "tags" : tags
    }

    return HttpResponse(template.render(context, request))







