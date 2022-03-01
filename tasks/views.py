from django.shortcuts import render
from .forms import TaskForm


def index(request):
    tasks = TaskForm()
    context = {
        "task_form" : tasks 
    }
    return render(request, "tasks/index.html",context)


def about(request):
    return render(request, "tasks/about.html")


