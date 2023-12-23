from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from ..models import  Tags
from ..forms import  create_new_tag, edit_tag
from django.utils.text import slugify

def add_new_tag(request):
    if request.method == "POST":
        form = create_new_tag(request.POST)

        if form.is_valid():
            name = slugify(form.cleaned_data["name"], allow_unicode=True)
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
    tag = get_object_or_404(Tags, id=id)

    pages = tag.pages.all()

    template = loader.get_template("tag_page.html")

    context = {
        "tag" : tag,
        "pages" : pages
    }

    return HttpResponse(template.render(context, request))

def edit_tag_view(request, name, id):
    tag = get_object_or_404(Tags, id=id)

    if request.method == "POST":
        form = edit_tag(request.POST)

        if form.is_valid():
            name = slugify(form.cleaned_data["name"], allow_unicode=True)
            details = form.cleaned_data["details"]
            
            if details != "":
                tag.details = details
                tag.name = name
                tag.save()
            else:
                tag.name = name
                tag.save()
            
            return HttpResponseRedirect(f"/tag/{tag.id}/{tag.name}")
    
    else:
        form = edit_tag(initial={"name":tag.name, "details":tag.details})

        template = loader.get_template("edit_tag.html")

        context = {
            "form_tag" : form,
        }

        return HttpResponse(template.render(context, request))
        

def tag_glossary(request):
    tags = Tags.objects.all()

    template = loader.get_template("tag_glossary.html")

    context = {
        "tags" : tags
    }

    return HttpResponse(template.render(context, request))







