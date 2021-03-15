from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi, This is FIRSTAPPLICATION.")

def tv(request):
    context = {'tag_var': "tag_var"}
    return render(request, "FirstApp/First_temp.html", context)

def si(request):
    context = {'tag_var': "tag_var"}
    return render(request, "FirstApp/static_webpage.html", context)

def si1(request):
    context = {'tag_var': "tag_var"}
    return render(request, "FirstApp/static_img.html", context)

