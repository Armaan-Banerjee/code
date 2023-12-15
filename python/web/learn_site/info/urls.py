from django.urls import path
from .views.pages import info_index, handle_page_create, handle_page_get
from .views.tags import add_new_tag, show_tag_details, tag_glossary

urlpatterns = [
    path("", info_index, name="users"),
    path("page/<uuid:id>/<str:title>", handle_page_get, name="get_page"),
    path("page/add", handle_page_create, name="post_page"),
    path("tags/add", add_new_tag, name="addign tags"),
    path("tag/<uuid:id>/<str:name>", show_tag_details, name="tag glossary"),
    path("tags/glossary", tag_glossary, name="tag glossary"),
]