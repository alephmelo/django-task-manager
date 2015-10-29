from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def dashboard(request):
	results = Task.objects.all()
	return render(request, 'home.html', {'results': results})