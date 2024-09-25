from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from todo_app.models import Tag, Task


class AdminSiteTest(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username="admin", password="password", email="admin@example.com"
        )
        self.client.login(username="admin", password="password")

        self.tag = Tag.objects.create(name="Test Tag")
        self.task = Task.objects.create(content="Test Task", is_done=False)
        self.task.tags.add(self.tag)

    def test_tag_admin_list_view(self):
        response = self.client.get(reverse("admin:todo_app_tag_changelist"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Tag")

    def test_task_admin_list_view(self):
        response = self.client.get(reverse("admin:todo_app_task_changelist"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")

    def test_task_admin_search(self):
        response = self.client.get(
            reverse("admin:todo_app_task_changelist"), {"q": "Test Task"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")

    def test_task_admin_filter(self):
        response = self.client.get(
            reverse("admin:todo_app_task_changelist"), {"tags": self.tag.pk}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")
