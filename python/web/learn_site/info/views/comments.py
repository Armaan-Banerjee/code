from ..models import Comment, Pages
from users.models import User
from ..forms import create_comment
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


@login_required
@require_POST
def create_comment_view(request):
    user = request.user

    form = create_comment(request.POST)

    if form.is_valid():

        # params = request.POST.dict()
        # print(params)
        # try:
        #     user_id = params["user_id"]
        #     page_id = params["page_id"]
        # except KeyError:
        #     html_content = "<a href='/'><button>home</button></a><p>no user id or page id</p>"
        #     return HttpResponse(html_content, content_type="text/html")
        
        user_id = form.cleaned_data["user_id"]
        page_id = form.cleaned_data["page_id"]

        user = get_object_or_404(User, id=user_id)
        page = get_object_or_404(Pages, id=page_id)

        text = form.cleaned_data["text"]
        Comment.add_comment(text=text, user=user, page=page)

        return HttpResponseRedirect(f"/page/{page_id}/comment_add")
    
def comments_views(request):
    return HttpResponse("responding")
    

