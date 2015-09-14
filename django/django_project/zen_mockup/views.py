from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def zen_mockup(request):
    return render(request, 'zen_mockup.html')