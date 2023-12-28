from django.urls import path
from .views.pages import info_index, handle_page_create, handle_page_get
from .views.tags import add_new_tag, show_tag_details, tag_glossary, edit_tag_view
from .views.comments import create_comment_view, comments_views

urlpatterns = [
    path("", info_index, name="users"),
    path("page/<uuid:id>/<str:title>", handle_page_get, name="get_page"),
    path("page/add", handle_page_create, name="post_page"),
    path("tags/add", add_new_tag, name="adding tags"),
    path("tag/<uuid:id>/<str:name>", show_tag_details, name="tag glossary"),
    path("tags/glossary", tag_glossary, name="tag glossary"),
    path("tags/edit/<uuid:id>/<str:name>", edit_tag_view, name="edit tag"),
    path("comments/add", create_comment_view, name="comment add"),
    path("comments/all", comments_views, name="all comments")
]