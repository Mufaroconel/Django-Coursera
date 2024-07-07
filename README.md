# Django-Coursera
Django Coursera Repository: A comprehensive collection of notes, code snippets, exercise solutions, and projects documenting my journey through Coursera's Django courses. Explore detailed module notes, review code samples, and analyze projects to deepen understanding and enhance Django skills. Join me in this learning adventure!


Here's an overview of how to set up a Django app and build a full-stack application:

### Setting Up a Django Project

1. **Install Django**:
   - Open your terminal and install Django using pip:
     ```bash
     pip install django
     ```
2. **Create a New Django Project**:
   - Create a new directory for your project and navigate into it:
     ```bash
     mkdir myproject
     cd myproject
     ```

   - Run the following command to create a new Django project:
     ```bash
     django-admin startproject myproject
     ```

   - This will create a basic directory structure for your project.

3. **Create a New Django App**:
   - Navigate into the project directory:
     ```bash
     cd myproject
     ```

   - Create a new Django app within the project:
     ```bash
     python manage.py startapp myapp
     ```

   - This will create a new directory for your app within the project directory.

### Setting Up the Virtual Environment (venv)

1. **Install Virtualenv**:
   - Install virtualenv using pip:
     ```bash
     pip install virtualenv
     ```

2. **Create a Virtual Environment**:
   - Navigate into the project directory:
     ```bash
     cd myproject
     ```

   - Create a new virtual environment:
     ```bash
     virtualenv venv
     ```

   - Activate the virtual environment:
     ```bash
     source venv/bin/activate
     ```

   - You should see the name of the virtual environment in your terminal prompt.

### Creating Models

1. **Create Models**:
   - Navigate into the app directory:
     ```bash
     cd myapp
     ```

   - Create a new file for your models:
     ```bash
     touch models.py
     ```

   - Define your models within the file:
     ```python
     # models.py
     from django.db import models

     class Book(models.Model):
         title = models.CharField(max_length=200)
         author = models.CharField(max_length=100)
         publication_date = models.DateField()
     ```

   - Run the following command to create the database tables for your models:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

### Creating Views

1. **Create Views**:
   - Navigate into the app directory:
     ```bash
     cd myapp
     ```

   - Create a new file for your views:
     ```bash
     touch views.py
     ```

   - Define your views within the file:
     ```python
     # views.py
     from django.shortcuts import render
     from .models import Book

     def book_list(request):
         books = Book.objects.all()
         return render(request, 'book_list.html', {'books': books})
     ```

### Creating Templates

1. **Create Templates**:
   - Navigate into the app directory:
     ```bash
     cd myapp
     ```

   - Create a new directory for your templates:
     ```bash
     mkdir templates
     ```

   - Navigate into the templates directory:
     ```bash
     cd templates
     ```

   - Create a new file for your template:
     ```bash
     touch book_list.html
     ```

   - Define your template within the file:
     ```html
     <!-- book_list.html -->
     <h1>Book List</h1>
     <ul>
     {% for book in books %}
         <li>{{ book.title }} ({{ book.author }})</li>
     {% endfor %}
     </ul>
     ```

### Creating URLs

1. **Create URLs**:
   - Navigate into the app directory:
     ```bash
     cd myapp
     ```

   - Create a new file for your URLs:
     ```bash
     touch urls.py
     ```

   - Define your URLs within the file:
     ```python
     # urls.py
     from django.urls import path
     from . import views

     urlpatterns = [
         path('books/', views.book_list, name='book_list'),
     ]
     ```

### Running the Server

1. **Run the Server**:
   - Navigate into the project directory:
     ```bash
     cd myproject
     ```

   - Run the following command to start the Django development server:
     ```bash
     python manage.py runserver
     ```

   - Open a web browser and navigate to `http://localhost:8000/books/` to see your book list.

This is a basic overview of how to set up a Django project and build a full-stack application. You can add more functionality and features as needed.

