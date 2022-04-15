from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sform", views.simple_form, name="sform"),
]
