from django.urls import path

from todo_app.views import HomePageTaskView, TagListView

urlpatterns = [
    path("", HomePageTaskView.as_view(), name="homepage"),
    path("tags/", TagListView.as_view(), name="tags"),

]

app_name = "todo"