from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Task

def home(request):
    if request.user.is_authenticated():
        return dashboard(request)
    else:
        return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def dashboard(request):
	results = Task.objects.all()
	return render(request, 'dashboard.html', {'results': results})
