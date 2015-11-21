from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Task
from django.contrib.auth.models import User
from .forms import TaskForm, TaskEditForm
import datetime

def home(request):
    """
    Display an individual home page.
    """
    if request.user.is_authenticated():
        return dashboard(request)
    else:
        return render(request, 'home.html')

def contact(request):
    '''
    Display contact page.
    '''
    return render(request, 'contact.html')

@login_required
def dashboard(request):
    """
    Display dashboard

    ``Task``
        An instance of Task Model.
    """
    results = Task.objects.all()
    nows = datetime.datetime.now()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=True)
            new_task.user = User.objects.get(username=request.user)
            new_task.save()
            return HttpResponseRedirect(reverse('core:home'))
    else:
        form = TaskForm()

    return render(request, 'dashboard.html', {'form': form, 'results': results, 'nows':nows})

@login_required
def edit_task(request, id):
    """
    Display edit task template.

    ``Task``
        An instance of Task Model.
    """
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskEditForm(request.POST, instance=task)
        if form.is_valid():
            new_task = form.save(commit=True)
            new_task.user = User.objects.get(username=request.user)
            new_task.save()
            return HttpResponseRedirect(reverse('core:home'))
    else:
        form = TaskEditForm(instance=task)
    return render(request, 'edit_task.html', {'task': task, 'form': form})

@login_required
def delete_task(request, id):
    """
    Delete task by id.

    ``Task``
        An instance of Task Model.
    """
    task = get_object_or_404(Task, id=id)
    task.delete()
    return HttpResponseRedirect(reverse('core:dashboard'))

