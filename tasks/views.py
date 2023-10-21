from datetime import datetime
from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home.html')

@login_required(login_url='login_user')
def tasks(request):
    current = Task.objects.filter(user=request.user, complete_date__isnull=True)
    completed = Task.objects.filter(user=request.user, complete_date__isnull=False)
    return render(request, 'tasks.html',{'current':current, 'completed':completed})

@login_required(login_url='login_user')
def create_task(request):
    if request.method =='GET':
        return render(request, 'create_task.html', {'form':TaskForm})
    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks')
        else:
            error = 'Something went wrong'

@login_required (login_url='login_user')           
def detail_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'GET':
        form = TaskForm(instance=task)
        return render(request, 'detail_task.html', {'form':form,'task': task})
    else:
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
        else:
            error = 'Something went wrong'
            return render(request, 'detail_task.html', {'form':form,'task': task, 'error':error})

@login_required(login_url='login_user')
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('tasks')

@login_required(login_url='login_user')
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.complete_date = timezone.now()
    task.save()
    return redirect('tasks')
