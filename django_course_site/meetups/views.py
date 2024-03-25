from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

## By HttpResponse
## I want to return the reponse to the browser
#
# def index(request):
#     return HttpResponse('Hello World!')

## By render template
def index(request):
    
    meetups = [
        { 'title': 'A First Meetup'},
        { 'title': 'A Second Meetup'}
    ]
    
    return render(request, 'meetups/index.html', {
        'meetups': meetups,
        'show_meetups': True
    }) 
## we have to give path start from inside templates
## NOT!! 'templates/meetups/index.html'