import io
from contextlib import redirect_stdout

from linkedlist import LinkedList
from tests.fixture import data

class TestLinkedList:
    def setup_method(self):
        self.ll = LinkedList()

    def catch_print(self, value=None):
        output = io.StringIO()
        with redirect_stdout(output):
            self.ll.pop(value)
            return output

    def test_append(self, data):
        for teacher in data:
            self.ll.append(teacher)
        assert self.ll.head is not None
        assert self.ll.head.data.get_name == 'John'
        assert self.ll.head.data.get_lastname == 'Deere'
        assert self.ll.head.data.get_education == "Bachelor's Degree"
        assert self.ll.head.data.get_experience == 15
        assert self.ll.head.data.get_discipline == 'mathmatics'
        assert self.ll.head.data.get_job_title == 'teacher'

    def test_pop(self, data):
        for teacher in data:
            self.ll.append(teacher)

        output = self.catch_print(self.ll.head.next_node.data)
        assert '\nУчитель Jessica, Parker удалён.\n' == output.getvalue()

        output = self.catch_print()
        assert 'Данных нет...\n' == output.getvalue()

        for i in range(3):
            self.catch_print(self.ll.head.data)
        output = self.catch_print(None)
        assert 'Список пуст...\n' == output.getvalue()

    def test_pop_empty(self):
        output = self.catch_print(None)
        assert 'Список пуст...\n' == output.getvalue()

    def test_view_data(self):
        assert self.ll.view_data() is None