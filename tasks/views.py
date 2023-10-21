from django.shortcuts import render
from .models import Task

def home(request):
    return render(request,'home.html')

def tasks(request):
    all_tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks.html',{'tasks':all_tasks})
