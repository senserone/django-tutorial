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