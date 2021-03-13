from django.urls import path, include
from . import views

urlpatterns = [
    path("firstapp/", views.index, name="Simple_Text"),
    path("template/", views.tv, name="TEMPLATE_PATH"),
    path("webpage/", views.si, name="Static_Image_file"),
]