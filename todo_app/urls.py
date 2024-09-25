from django.urls import path

from todo_app.views import HomePageTaskView, TagListView, TaskCreateView, TaskUpdateView, task_status, TagCreateView, \
    TagUpdateView

urlpatterns = [
    path("", HomePageTaskView.as_view(), name="homepage"),
    path("tags/", TagListView.as_view(), name="tags"),
    path("tags/create", TagCreateView.as_view(), name="tag_create"),
    path("tags/<int:pk>/update",TagUpdateView.as_view(), name="tag_update"),
    path("task/create/", TaskCreateView.as_view(), name="task_create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    path("task/toggle_status/<int:pk>/", task_status, name="task_status"),

]

app_name = "todo"