from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item


# Create your views here.


def index(response):
    return render(response, "kangaroo/home.html", {})

def index2(response):
    ls = ToDoList.objects.get(id = 1)
    items = ls.item_set.all
    return render(response, "kangaroo/list.html", {"list":ls, "listname":ls.name})

def index3(response):
    return render(response, "kangaroo/index.html", {})

def todolist(response, id):
    todolist = ToDoList.objects.get(id = id)
    item = todolist.item_set.get(id = 1)
    return HttpResponse("<h1>%s</h1><body>%s<body>" % (todolist.name, str(item.text)))
