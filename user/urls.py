from django.urls import path, include
from user.views import profile

urlpatterns = [
    path("", profile),
]