from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("giraffe1/", views.index2, name = "index2"),
    path("todolist<int:id>/", views.todolist, name = "todolist"),
    path("alex", views.index3, name = "index3")
]