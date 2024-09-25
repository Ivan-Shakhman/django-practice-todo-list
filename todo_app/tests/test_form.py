from django.test import TestCase
from todo_app.forms import TaskForm, TagForm
from todo_app.models import Task, Tag


class TaskFormTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'content': 'Test Task',
            'deadline': '2024-12-31',
            'tags': []
        }

    def test_invalid_task_form_without_content(self):
        form = TaskForm(data={'content': '', 'deadline': '2024-12-31'})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)

    def test_task_form_date_widget(self):
        form = TaskForm()
        self.assertIn('type="date"', str(form['deadline']))


class TagFormTest(TestCase):
    def test_valid_tag_form(self):
        form = TagForm(data={'name': 'Test Tag'})
        self.assertTrue(form.is_valid())
        tag = form.save()
        self.assertEqual(tag.name, 'Test Tag')

    def test_invalid_tag_form_without_name(self):
        form = TagForm(data={'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)