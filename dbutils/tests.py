from django.test import TestCase
from .utils import DBUtils
from manager.models import Task
from datetime import date

class DBUtilsTest(TestCase):
    def setUp(self) -> None:
        self.db = DBUtils
        self.task = Task
        self.finish_date = date.today()

    def test_crud_test(self):
        self.assertEqual(self.db.create_task(self.task, 'task', self.finish_date, 'username'), 1)
        self.assertEqual(self.db.update_task(self.task, 1, "new_task", self.finish_date, 'new_username'), 1)
        self.assertEqual(self.db.delete_task(self.task, 1), 1)
