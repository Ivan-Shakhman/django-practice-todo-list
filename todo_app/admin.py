from django.contrib import admin

from todo_app.models import Tag, Task

admin.site.register(Tag)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ["content"]
    list_filter = ["tags"]
