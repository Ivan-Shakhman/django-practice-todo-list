from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from todo_app.models import Task, Tag

User = get_user_model()


class TaskViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")

        self.tag = Tag.objects.create(name="Test Tag")
        self.task = Task.objects.create(content="Test Task")
        self.task.tags.add(self.tag)

    def test_home_page_view(self):
        response = self.client.get(reverse("todo:homepage"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo_app/task_list.html")

    def test_tag_create_view(self):
        response = self.client.post(
            reverse("todo:tag_create"),
            {
                "name": "New Tag",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Tag.objects.filter(name="New Tag").exists())

    def test_task_delete_view(self):
        response = self.client.post(reverse("todo:task_delete", args=[self.task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

    def test_tag_list_view(self):
        response = self.client.get(reverse("todo:tags"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo_app/tag_list.html")

    def test_task_status_view(self):
        response = self.client.get(reverse("todo:task_status", args=[self.task.id]))
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_done)
