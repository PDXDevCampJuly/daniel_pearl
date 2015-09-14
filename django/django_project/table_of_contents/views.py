from django.shortcuts import render
from django.http import HttpResponse

def table_of_contents(request):
    return render(request, "table_of_contents.html")