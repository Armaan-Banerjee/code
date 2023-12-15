from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from ..models import page, Tags
from ..forms import create_new_page, create_new_tag

def info_index(request):
    pages = page.objects.all().values()
    template = loader.get_template('index.html')

    context = {
        "pages" : pages
    }
    return HttpResponse(template.render(context, request))

def handle_page_get(request, id, title):
    page_get = page.objects.get(id=id)

    tags = page_get.show_tags()

    template = loader.get_template("default_Page.html")

    context = {
        "page" : page_get, 
        "tags" : tags
    }

    return HttpResponse(template.render(context, request))

def handle_page_create(request):


    if request.method == "POST":
        form = create_new_page(request.POST)

        if form.is_valid():
            data = form.cleaned_data
    
            tags = form.cleaned_data["tags"]
            

            new_page = page(title=data["title"], data=data["data"])

            list_t = []
            for tag in tags:
                real_t = Tags.objects.get(id=tag)
                list_t.append(real_t)

            new_page.tags.set(list_t)

            new_page.save()

            id = new_page.id
            title = new_page.title

            return HttpResponseRedirect(f"/page/{id}/{title}")
    
    else:
        form = create_new_page()

        #print(form)

        form_tag = create_new_tag()

        template = loader.get_template("add_page.html")

        context = {
            "form_tag" : form_tag,
            "form" : form
        }

        return HttpResponse(template.render(context, request))
    