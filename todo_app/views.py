from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_app.forms import TaskForm
from todo_app.models import Task, Tag


class HomePageTaskView(generic.ListView):
    model = Task
    paginate_by = 6



class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('todo:homepage')


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:homepage")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 6


