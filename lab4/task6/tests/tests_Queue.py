import unittest
from lab4.task6.src.Queue_Realization import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        """Создание новой очереди размером 3 перед каждым тестом"""
        self.queue = Queue(max_size=3)

    def test_isEmpty(self):
        """Тест метода isEmpty"""
        self.assertEqual(self.queue.isEmpty(), True)
        self.queue.enQueue(1)
        self.assertFalse(self.queue.isEmpty(), False)

    def test_isFull(self):
        """Тест метода isFull"""
        self.assertFalse(self.queue.isFull())
        self.queue.enQueue(1)
        self.queue.enQueue(2)
        self.queue.enQueue(3)
        self.assertTrue(self.queue.isFull())

    def test_enQueue(self):
        """Тест метода enQueue"""
        self.queue.enQueue(1)
        self.assertEqual(self.queue.display_queue(), "1")
        self.queue.enQueue(2)
        self.assertEqual(self.queue.display_queue(), "1, 2")
        self.queue.enQueue(3)
        self.assertEqual(self.queue.display_queue(), "1, 2, 3")

    def test_deQueue(self):
        """Тест метода deQueue"""
        self.queue.enQueue(1)
        self.queue.enQueue(2)
        self.queue.enQueue(3)
        self.queue.deQueue()
        self.assertEqual(self.queue.display_queue(), "2, 3")
        self.queue.deQueue()
        self.assertEqual(self.queue.display_queue(), "3")
        self.queue.deQueue()
        self.assertTrue(self.queue.isEmpty())

    def test_display_queue(self):
        """Тест метода display_queue"""
        self.queue.enQueue(1)
        self.queue.enQueue(2)
        self.queue.enQueue(3)
        self.assertEqual(self.queue.display_queue(), "1, 2, 3")
        self.queue.deQueue()
        self.assertEqual(self.queue.display_queue(), "2, 3")






