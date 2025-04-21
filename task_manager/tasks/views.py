from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def create_task(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('task-list')  # ✅ fixed
    return render(request, 'create_task.html', {'form': form})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('task-list')  # ✅ fixed
    return render(request, 'update_task.html', {'form': form})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task-list')  # already correct
    return render(request, 'delete_task.html', {'task': task})
