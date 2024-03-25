# SETUP #
init venv
>> python venv .venv

install django
>> python -m pip install Django

# NEW PROJECT #
create new project
>> django-admin startproject [project_name]

# NEW APP #
1. create new app
>> python manage.py startapp [app_name]

2. add app to INSTALLED_APPS in settings.py
3. create urls.py in new app
4. don't forget to make "project url.py" know "New App Urls.py"

# RUN SERVER #
>> python manage.py runserver

# TEMPLATE (this method is a good practice)
>> create folder "templates" inside APP Folder

`NOTE`: You can see in "settings.py". There is TEMPLATES section
and it's given 'APP_DIRS': True which tell your project to see templates inside APP Folder, We can add Extra Templates Directory across multiple app by give inside 'DIRS':[]

>> create app name folder inside "templates" folder again
>> app-name/templates/app-name

`NOTE` we have to do this because it prevent from app crashing of multiple apps and they have templates with similar name
>> then we create templates html file inside
>> app-name/templates/app-name/index.html

# STATIC FILE
when we want to add CSS or Javascript or images to HTML file
these are called "static" contents
>> creating static folder like creating templates folder
>> app-name/static/app-name
inside this folder you can add folders
    - images
    - scripts
    - styles
>> to import css to html file
>> first 
{% load static %} `on the first line of html file`
<link rel="stylesheet" href="{% static 'meetups/styles/base.css' %}"> after <title> tag
>> like templates we will reference the path which start from inside 'static' folder

# Transfer data from View To Template
`in View `
def index(request):
    
    meetups = [
        { 'title': 'A First Meetup'},
        { 'title': 'A Second Meetup'}
    ]
    
    return render(request, 'meetups/index.html', {
        'meetups': meetups,
    }) 
`in Template`
<h2>{{ meetups.0.title }}</h2> <!-- Interpolation Syntax -->