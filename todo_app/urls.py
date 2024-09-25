from django.urls import path

from todo_app.views import HomePageTaskView, TagListView, TaskCreateView, TaskUpdateView

urlpatterns = [
    path("", HomePageTaskView.as_view(), name="homepage"),
    path("tags/", TagListView.as_view(), name="tags"),
    path("task/create/", TaskCreateView.as_view(), name="task_create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),

]

app_name = "todo"