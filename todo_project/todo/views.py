from django.shortcuts import render, redirect, get_object_or_404  # Import get_object_or_404
from .models import Task
from .forms import TaskForm

def home(request):
    tasks = Task.objects.all()  # Fetch all tasks from the database
    return render(request, 'todo/home.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after creating the task
    else:
        form = TaskForm()
    return render(request, 'todo/create_task.html', {'form': form})

# View to update a task
def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)  # Fetch the task by ID
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/update_task.html', {'form': form, 'task': task})

# View to delete a task
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)  # Fetch the task by ID
    if request.method == 'POST':
        task.delete()  # Delete the task
        return redirect('home')
    return render(request, 'todo/delete_task.html', {'task': task})
