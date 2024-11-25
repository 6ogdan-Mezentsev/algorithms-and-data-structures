import unittest
from lab4.task6.src.Stack_Realization import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        """Создание нового стека перед каждым тестом"""
        self.stack = Stack()

    def test_isEmpty(self):
        """Тест метода isEmpty"""

        self.assertEqual(self.stack.isEmpty(), True)
        self.stack.push(1)
        self.assertFalse(self.stack.isEmpty(), False)

    def test_Push(self):
        """Тест метода Push"""
        self.stack.push(1)
        self.assertEqual(self.stack.top.value, 1)
        self.stack.push(2)
        self.assertEqual(self.stack.top.value, 2)
        self.assertEqual(self.stack.top.next.value, 1)

    def test_Pop(self):
        """Тест метода Pop"""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        popped_value = self.stack.pop()
        self.assertEqual(popped_value, 3)
        self.assertEqual(self.stack.top.value, 2)
        popped_value = self.stack.pop()
        self.assertEqual(popped_value, 2)
        self.assertEqual(self.stack.top.value, 1)

    def test_display_stack(self):
        """Тест метода display_stack"""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        display_stack = self.stack.display_stack()
        self.assertEqual(display_stack, "3, 2, 1")





