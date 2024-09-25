from django.urls import path

from todo_app.views import HomePageTaskView

urlpatterns = [
    path('', HomePageTaskView.as_view(), name='homepage'),

]

app_name = "todo"