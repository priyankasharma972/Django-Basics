# Django-Basics
This repository contains the basics of Python Framework-Django which includes the normal views and Class-based Views.

Below are the initial steps to start:-
	1. To set up project:-
	django-admin startproject 'project-name'
	
	2. To Run server:-
	python manage.py runserver
	
	3. Next Command for all the database related and other set up:-
	python manage.py migrate
	
	4. Login to Django Admin Command and create user details:-
	python manage.py createsuperuser
	
	5. Adding a new application(app):-
	python manage.py startapp 'app-name'
	
	6. After adding the models.py run the below command:-
  python manage.py makemigrations
	Before this, make sure that the new Application is also added to the `settings page` under Installed Apps section
	
	7. Next Command:- python manage.py migrate

