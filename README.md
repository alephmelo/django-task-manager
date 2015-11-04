# Just To Do It!

## Django-powered todo list

This task manager helps you to get things done. And also, is a quite good django intro for beginners. This repo contains the CRUD (Create, Retrieve, Update, Delete) concept, with this concept you can create basic Django applications and understand how a few things work, like urls, views, models and so on. 

### Usage
* Clone the repo.
```git
git clone git@github.com:alephmelo/django-task-manager.git
```
* Install packages with pip
```
pip install requirements.txt
```
* Create database (Django default is sqlite3)
```
python manage.py migrate
```
* Create super user to use Django-Admin
```
python manage.py createsuperuser
```
* Run for the win!
```
python manage.py runserver
```
-----------------------------------------------

### To do:
* Create views and forms to add tasks ✅
* Create view to edit task by id ✅
* Create view to delete task by id ✅
* Create boolean attribute into Task Model to check if the task was finished
* Differ tasks from users in the system.
