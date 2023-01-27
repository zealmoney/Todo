from django.test import TestCase

from .models import Todo

class TodoModelTest(TestCase):
    """Test the todo model"""
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title = 'first to do',
            body = 'a body of text here'
        )
    
    def test_model_content(self):
        self.assertEqual(self.todo.title, 'first to do')
        self.assertEqual(self.todo.body, 'a body of text here')
        self.assertEqual(str(self.todo), 'first to do')
