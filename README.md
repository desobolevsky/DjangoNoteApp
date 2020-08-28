# DjangoNoteApp
DjangoNoteApp is a note-taking Django Application which allows you to create, change and share your notes. 

# Installation
In order to get the project for review, editing or testing, clone project:
```sh
$ git clone https://github.com/desobolevsky/DjangoNoteApp.git
```
Create a new virtual environment and install the dependencies:
```sh
$ cd DjangoNoteApp
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
Apply migrations:
```sh
$ python Notes/manage.py migrate
```
Run a server:
```sh
$ python Notes/manage.py runserver 8000
```
Now the application is running on http://localhost:8000/. Enjoy ;)

# Todos
- Add e-mail verification
- Add user note sharing system
- Add image, audio etc functionality in note-taking process

