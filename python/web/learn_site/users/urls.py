from django.urls import path, include
from . import views

urlpatterns = [
    path("user/", views.index, name="users"),
    path("user/<uuid:id>", views.public_info),
    path('accounts/', include('django.contrib.auth.urls')),
]