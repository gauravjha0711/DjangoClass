print("1");

# py-menv <name> //for creating a virtual environment
# \.venv\Scripts\activate.bat          //for activating the virtual environment
# pip install django                   //for installing django 
# django-admin --version              //for checking the version of django
# django-admin startproject day7_29        //for creating a project
# python manage.py startapp first   or  django-admin startapp first(fresh application)  --  //for creating an app
# python manage.py runserver             //for running the server

work flow:
manage.py->settings.py->urls.py(project)->urls.py(app)->views.py->http.response