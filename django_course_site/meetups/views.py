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
        { 'title': 'A First Meetup', 'location': 'New York', 'slug': 'a-first-meetup'},
        { 'title': 'A Second Meetup','location': 'Paris', 'slug': 'a-second-meetup'}
    ]
    
    return render(request, 'meetups/index.html', {
        'meetups': meetups,
        'show_meetups': True
    }) 
## we have to give path start from inside templates
## NOT!! 'templates/meetups/index.html'

def meetup_details(request, meetup_slug): #same name as slug:<____> in urls.py
    print(meetup_slug)
    selected_meetup = {'title': 'A First Meetup',
                       'description': 'This is a First Meetup'}
    return render(request, 'meetups/meetup-details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description'],
    })