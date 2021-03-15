from django.urls import path, include
from . import views

urlpatterns = [
    path("first/", views.index, name="Simple_Text"),
    path("temp/", views.tv, name="TEMPLATE_PATH"),
    path("web/", views.si, name="Static_Image_file"),
    path("my/", views.si1, name="Static_Image_file"),
]