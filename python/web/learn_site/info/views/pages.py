from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from ..models import Pages, Tags
from ..forms import create_new_page, create_new_tag, create_comment
from django.utils.text import slugify
from users.models import Bookmark

def info_index(request):
    pages = Pages.objects.all().values()
    tags = Tags.objects.all()
    template = loader.get_template('index.html')

    context = {
        "pages" : pages,
        "tags": tags
    }

    # print(request.GET.dict())

    return HttpResponse(template.render(context, request))

def handle_page_get(request, id, title):
    page_get = get_object_or_404(Pages, id=id)

    tags = page_get.Tags.all()

    comment_form = create_comment(initial={"user_id":request.user.id, "page_id":page_get.id})

    comments = page_get.comment_set.all()

    bookmarked = False
    if request.user.is_authenticated:
        bookmarks = request.user.bookmark_set.all()
        for bookmark in bookmarks:
            if bookmark.page_id == page_get.id:
                bookmarked = True
    

    template = loader.get_template("default_Page.html")

    context = {
        "page" : page_get, 
        "tags" : tags,
        "comment_form": comment_form,
        "comments": comments,
        "bookmarked": bookmarked
    }

    return HttpResponse(template.render(context, request))

def handle_page_create(request):

    if request.method == "POST":
        form = create_new_page(request.POST)

        if form.is_valid():
            data = form.cleaned_data
    
            tags = form.cleaned_data["tags"]

            title = data["title"]
            title_slug = slugify(title, allow_unicode=True)

            new_page = Pages(title=title_slug, data=data["data"])

            new_page.save()

            for tag in tags:
                real_t = Tags.objects.get(id=tag)
                new_page.Tags.add(real_t)
            
            id = new_page.id
            title = new_page.title

            return HttpResponseRedirect(f"/page/{id}/{title}")
    
    else:
        form = create_new_page()

        #print(form)

        form_tag = create_new_tag()

        #print(form)
        #print(Tags.set_all())

        template = loader.get_template("add_page.html")

        context = {
            "form_tag" : form_tag,
            "form" : form
        }

        return HttpResponse(template.render(context, request))
    