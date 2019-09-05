from django.shortcuts import render

def index(request):
    """A iew that display the index page"""
    return render (request, "index.html")
