from ..models import Comment, Pages
from users.models import User
from ..forms import create_comment
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required

@login_required
def create_comment_view(request):
    user = request.user

    if request.method == "POST":
        
        form = create_comment(request.POST)

        if form.is_valid():

            params = request.POST.dict()
            print(params)
            try:
                user_id = params["user_id"]
                page_id = params["page_id"]
            except KeyError:
                html_content = "<a href='/'><button>home</button></a><p>no user id or page id</p>"
                return HttpResponse(html_content, content_type="text/html")

            user = get_object_or_404(User, id=user_id)
            page = get_object_or_404(Pages, id=page_id)

            text = form.cleaned_data["text"]
            Comment.add_comment(text=text, user=user, page=page)

            return HttpResponseRedirect(f"/pages/{page_id}/comment_add")
    
    else:
        return HttpResponse("forbidden")

    

