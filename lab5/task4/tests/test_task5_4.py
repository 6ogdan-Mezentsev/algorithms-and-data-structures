import unittest
from lab5.utils import count_time_and_memory
from lab5.task4.src.heapSort_reverse import *
import random


class AlgorithmsHeapTestCase(unittest.TestCase):

    def test_should_check_success_heapSort_reverse(self):
        # given
        n = 100000
        A = random.sample(range(1, 10 ** 9), n)  # Генерируем случайный массив случайных чисел
        expected_result = sorted(A, reverse=True)

        # when
        result, elapsed_time, memory_used = count_time_and_memory(heap_sort_reverse, n, A)

        # then
        self.assertEqual(result, expected_result)
        self.assertLess(elapsed_time, 3)
        self.assertLess(memory_used, 266144)

