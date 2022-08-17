from django.shortcuts import render, redirect
from . models import *
from . forms import TaskForm

# Create your views here.

def home(request, pk = None):
    if pk != None:
        task = Task.objects.get(id = pk)
        if request.POST.get('delete') == 'delete':
            task.delete()

        elif request.POST.get('edit') == 'edit':
            form = TaskForm(instance = task)

            return render(request, 'app1/update.html', {'form': form, 'task': task})  

        elif request.POST.get('update') == 'update':
            form = TaskForm(request.POST, instance = task)
            if form.is_valid():
                form.save()          

    else:  
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

    form = TaskForm
    task_list = list(Task.objects.all().values())
    page = {
        'form': form,
        'task_list': task_list
    }

    return render(request, 'app1/home.html', page)
    
def list_view(request):
    task_list = list(Task.objects.all().values())
    task_dict = {'task_list': task_list}
    
    return render(request, 'app1/forms.html', task_dict)

def create(request):
    name = request.POST.get('name')
    content = request.POST.get('content')
    task_dict = {'name': name, 'content': content}
    task = Task(**task_dict)
    task.save()

    return redirect('list_view')

def edit(request, pk):
    task = Task.objects.get(id = pk)
    task_dict = {'id': task.id, 'name': task.name, 'content': task.content}

    return render(request, 'app1/edit.html', task_dict)

def update(request, pk):
    task = Task.objects.get(id = pk)
    task.name = request.POST.get('name')
    task.content = request.POST.get('content')
    task.save()

    return redirect('list_view')

def delete(request, pk):
    task = Task.objects.get(id = pk)
    task.delete()

    return redirect('list_view')
