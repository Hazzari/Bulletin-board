from django.urls import path

from .views import bbs

urlpatterns = [
    path('bbs/', bbs)
]
