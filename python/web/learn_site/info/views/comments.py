from ..models import Comment, Pages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required

@login_required
def create_comment(request):
    user = request.user
    