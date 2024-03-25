from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

## By HttpResponse
# def index(request):
#     # I want to return the reponse to the browser
#     return HttpResponse('Hello World!')

## By render template
def index(request):
    return render(request, 'meetups/index.html') 
# we have to give path start from inside templates
# NOT!! 'templates/meetups/index.html'