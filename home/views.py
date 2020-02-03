from django.shortcuts import render

# Create your views here.
def index(request):
    """This is a view that shows the index page"""
    return render(request, "index.html")