from django.shortcuts import render

def table_of_contents(request):
    return render(request, "table_of_contents.html")