from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from . import models

def index(request):
    if request.method == 'POST':
        title = request.POST['title']
        status = False

        obj = models.Todo(title=title, status=status)
        obj.save()

        return HttpResponse(
            f"Nova atividade criada {obj.title}, {status}, {obj.id}"
        )

    todos = models.Todo.objects.all()

    template = loader.get_template('microapp/index.html')

    return HttpResponse(template.render({"todos": todos}, request))


def edit(request, id=None):
    if request.method == 'POST':
        id = request.POST['id']
        title = request.POST['title']
        status = request.POST['status']

        todo = models.Todo.objects.get(id=id)
        todo.title = title
        todo.status = status

        todo.save()

        return HttpResponseRedirect('/todos/')

    template = loader.get_template('microapp/edit.html')

    todos_filtered = models.Todo.objects.filter(id=id)

    if len(todos_filtered) == 0:
        return HttpResponse(f"Atividade de id = {id} não existe")

    todo = todos_filtered[0]

    return HttpResponse(template.render({"todo": todo}, request))


def clean(requests):
    
    models.Todo.objects.all().delete()

    return HttpResponseRedirect('/todos/')
