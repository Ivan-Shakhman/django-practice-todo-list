from django.shortcuts import render
from django.views import generic

from todo_app.models import Task, Tag


class HomePageTaskView(generic.ListView):
    model = Task
    paginate_by = 6


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 6
