from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User

# Create your views here.

def index(request):
    users = User.objects.all().values()
    template = loader.get_template('glossary.html')
    context = {
        "users" : users
    }
    return HttpResponse(template.render(context, request))

def public_info(request, id):
    wanted_user = User.objects.get(id=id)
    template = loader.get_template("public_info.html")

    context = {
        "user" : wanted_user
    }

    return HttpResponse(template.render(context, request))