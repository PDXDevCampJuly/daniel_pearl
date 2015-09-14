from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    content = {'adjective': "rad"}
    return render(request, "index.html", content)

# Create your views here.

def corgis(request):
    return HttpResponse("corgis are awesome!")

def forum(request):
    return render(request, 'fake_post.html')
