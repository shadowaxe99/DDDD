import unittest
from app.models import Task

class TestModels(unittest.TestCase):
    def test_task_creation(self):
        task = Task.objects.create(title="Buy groceries", description="Buy milk, eggs, and bread")
        self.assertEqual(task.title, "Buy groceries")
        self.assertEqual(task.description, "Buy milk, eggs, and bread")
        self.assertFalse(task.completed)
        self.assertIsNone(task.due_date)

    def test_task_completion(self):
        task = Task.objects.create(title="Clean the house", description="Clean the living room and kitchen")
        task.complete()
        self.assertTrue(task.completed)

    def test_task_due_date(self):
        task = Task.objects.create(title="Finish report", description="Complete the quarterly report")
        task.set_due_date("2022-12-31")
        self.assertEqual(task.due_date, "2022-12-31")

if __name__ == '__main__':
    unittest.main()