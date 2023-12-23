from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import User, Bookmark
from info.models import Pages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def index(request):
    users = User.objects.all().values()
    template = loader.get_template('glossary.html')
    context = {
        "users" : users
    }
    return HttpResponse(template.render(context, request))

def public_info(request, id):
    wanted_user = get_object_or_404(User, id=id)
    template = loader.get_template("public_info.html")

    context = {
        "user" : wanted_user
    }

    return HttpResponse(template.render(context, request))

@csrf_exempt
def add_bookmark_view(request):
    if request.method == "POST":
        json_data = json.loads(request.body.decode('utf-8'))
        user_id = json_data["user_id"]
        page_id = json_data["page_id"]

        user = get_object_or_404(User, id=user_id)
        page = get_object_or_404(Pages, pk=page_id)

        bookmark = Bookmark.add_bookmark(user=user, page=page)

        return JsonResponse({"bookmark_id": bookmark.id})

@csrf_exempt
def delete_bookmark_view(request):
    if request.method == "POST":
        json_data = json.loads(request.body.decode("utf-8"))
        user_id = json_data["user_id"]
        page_id = json_data["page_id"]

        user = get_object_or_404(User, id=user_id)
        page = get_object_or_404(Pages, pk=page_id)

        bookmark = Bookmark.get_bookmark(user=user, page=page)

        try:
            bookmark.delete_bookmark()
            return JsonResponse({"deleted": True})
        except:
            return JsonResponse({"delted": False})



@login_required
def user_dashboard(request):
    user = request.user

    bookmarks = user.get_bookmarks()
    comments = user.get_comments()

    template = loader.get_template("dashboard.html")

    context = {
        "bookmarks": bookmarks,
        "comments": comments
    }

    return HttpResponse(template.render(context=context, request=request))


    


