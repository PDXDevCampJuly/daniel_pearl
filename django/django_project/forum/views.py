from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def forum(request):
    return render(request, 'fake_post.html')