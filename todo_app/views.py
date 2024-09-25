from django.shortcuts import render
from django.views import generic

from todo_app.models import Task


class HomePageTaskView(generic.ListView):
    model = Task
    paginate_by = 6
