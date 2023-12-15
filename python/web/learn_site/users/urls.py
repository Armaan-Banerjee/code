from django.urls import path
from . import views

urlpatterns = [
    path("user/", views.index, name="users"),
    path("user/<uuid:id>", views.public_info),
]