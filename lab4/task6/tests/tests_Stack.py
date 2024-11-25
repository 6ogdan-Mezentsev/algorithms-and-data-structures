import unittest
from lab4.task6.src.Stack_Realization import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        """Создание нового стека перед каждым тестом"""
        self.stack = Stack()

    def test_isEmpty(self):
        """Тест метода isEmpty"""
        # given
        expected_result1 = True
        expected_result2 = False
        # when
        self.assertEqual(self.stack.isEmpty(), expected_result1)
        self.stack.push(1)
        # then
        self.assertFalse(self.stack.isEmpty(), expected_result2)

    def test_Push(self):
        """Тест метода Push"""
        # when
        self.stack.push(1)
        self.assertEqual(self.stack.top.value, 1)
        self.stack.push(2)
        # then
        self.assertEqual(self.stack.top.value, 2)
        self.assertEqual(self.stack.top.next.value, 1)

    def test_Pop(self):
        """Тест метода Pop"""
        # given
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        # when
        popped_value = self.stack.pop()
        self.assertEqual(popped_value, 3)
        self.assertEqual(self.stack.top.value, 2)
        popped_value = self.stack.pop()
        # then
        self.assertEqual(popped_value, 2)
        self.assertEqual(self.stack.top.value, 1)

    def test_display_stack(self):
        """Тест метода display_stack"""
        # given
        expected_result = "3, 2, 1"
        # when
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        display_stack = self.stack.display_stack()
        # then
        self.assertEqual(display_stack, expected_result)





