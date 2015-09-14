from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def gallery(request):
    return render(request, "gallery.html")

def join(request):
    return render(request, "join.html")
