from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import User
from django.contrib.auth.decorators import login_required

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

@login_required
def user_dashboard(request):
    user = request.user

    bookmarks = user.bookmarks


