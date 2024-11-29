import unittest
from lab5.utils import count_time_and_memory
from lab5.task3.src.heap_sort import create_heap


class AlgorithmsHeapTestCase(unittest.TestCase):

    def test_should_check_success_create_heap(self):
        # given
        n = 5
        A = [7, 8, 3, 1, 6, 5]
        expected_result = [(1, 3), (0, 1), (1, 4)]

        # when
        result, elapsed_time, memory_used = count_time_and_memory(create_heap, n, A)

        # then
        self.assertEqual(result, expected_result)
        self.assertLess(elapsed_time, 3)
        self.assertLess(memory_used, 266144)

