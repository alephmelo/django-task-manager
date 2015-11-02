from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Task
from django.contrib.auth.models import User
from .forms import TaskForm

def home(request):
    if request.user.is_authenticated():
        return dashboard(request)
    else:
        return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

@login_required
def dashboard(request):
    results = Task.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=True)
            new_task.user = User.objects.get(username=request.user)
            new_task.save()
            return HttpResponseRedirect(reverse('core:home'))
    else:
        form = TaskForm()

    return render(request, 'dashboard.html', {'form': form, 'results': results})
