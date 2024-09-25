from django.test import TestCase
from todo_app.models import Tag, Task


class TagModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Test Tag")

    def test_tag_creation(self):
        self.assertEqual(self.tag.name, "Test Tag")
        self.assertEqual(str(self.tag), "Test Tag")


class TaskModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Test Tag")
        self.task = Task.objects.create(content="Test Task", is_done=False)
        self.task.tags.add(self.tag)

    def test_task_creation(self):
        self.assertEqual(self.task.content, "Test Task")
        self.assertFalse(self.task.is_done)
        self.assertIn(self.tag, self.task.tags.all())
        self.assertIsNotNone(self.task.created_at)

    def test_task_str(self):
        self.assertEqual(str(self.task), "Test Task")