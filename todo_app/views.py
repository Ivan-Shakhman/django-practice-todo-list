

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from todo_app.forms import TaskForm, TagForm
from todo_app.models import Task, Tag


class HomePageTaskView(generic.ListView):
    model = Task
    paginate_by = 6
    queryset = Task.objects.all().order_by('-is_done', '-created_at')



class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('todo:homepage')


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tags")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tags")

class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:homepage")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 6


def task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect(reverse("todo:homepage"))


