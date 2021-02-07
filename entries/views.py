from django.shortcuts import render
from .models import Book

def index(request): 
    entries = Book.objects.all()
    
    context = {'entries': entries}

    return render (request,  'entries/index.html', context ) 

def add(request):

    return render (request, 'entries/add.html' )