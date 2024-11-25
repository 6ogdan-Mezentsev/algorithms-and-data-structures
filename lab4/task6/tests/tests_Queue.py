import unittest
from lab4.task6.src.Queue_Realization import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        """Создание новой очереди размером 3 перед каждым тестом"""
        self.queue = Queue(max_size=3)

    def test_should_check_success_isEmpty(self):
        """Тест метода isEmpty"""
        # given
        expected_result1 = True
        expected_result2 = False
        # when
        self.assertEqual(self.queue.isEmpty(), expected_result1)
        self.queue.enQueue(1)
        # then
        self.assertEqual(self.queue.isEmpty(), expected_result2)

    def test_should_check_success_isFull(self):
        """Тест метода isFull"""
        # given
        self.assertFalse(self.queue.isFull())
        # when
        self.queue.enQueue(1)
        self.queue.enQueue(2)
        self.queue.enQueue(3)
        # then
        self.assertTrue(self.queue.isFull())

    def test_should_check_success_enQueue(self):
        """Тест метода enQueue"""
        # given
        expected_result1 = "1"
        expected_result2 = "1, 2"
        expected_result3 = "1, 2, 3"
        # when
        self.queue.enQueue(1)
        self.assertEqual(self.queue.display_queue(), expected_result1)
        self.queue.enQueue(2)
        self.assertEqual(self.queue.display_queue(), expected_result2)
        self.queue.enQueue(3)
        # then
        self.assertEqual(self.queue.display_queue(), expected_result3)

    def test_should_check_success_deQueue(self):
        """Тест метода deQueue"""
        # given
        self.queue.enQueue(1)
        self.queue.enQueue(2)
        self.queue.enQueue(3)
        expected_result1 = "2, 3"
        expected_result2 = "3"
        # when
        self.queue.deQueue()
        self.assertEqual(self.queue.display_queue(), expected_result1)
        self.queue.deQueue()
        self.assertEqual(self.queue.display_queue(), expected_result2)
        self.queue.deQueue()
        # then
        self.assertTrue(self.queue.isEmpty())

    def test_should_check_success_display_queue(self):
        """Тест метода display_queue"""
        # given
        self.queue.enQueue(1)
        self.queue.enQueue(2)
        self.queue.enQueue(3)
        expected_result1 = "1, 2, 3"
        expected_result2 = "2, 3"
        # when
        self.assertEqual(self.queue.display_queue(), expected_result1)
        self.queue.deQueue()
        # then
        self.assertEqual(self.queue.display_queue(), expected_result2)






