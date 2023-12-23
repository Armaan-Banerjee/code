from django.urls import path, include
from . import views

urlpatterns = [
    path("user/", views.index, name="users"),
    path("user/<uuid:id>", views.public_info),
    path("bookmark/add", views.add_bookmark_view),
    path("bookmark/delete", views.delete_bookmark_view),
    path("dashboard", views.user_dashboard),
    path('accounts/', include('django.contrib.auth.urls')),
]