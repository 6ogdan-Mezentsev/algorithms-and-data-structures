import unittest
from lab2.utils import count_time_and_memory
from lab2.task6.src.max_subarray import search_max_subarray


class AlgorithmsSortTestCase(unittest.TestCase):

    def test1_should_check_success_search_max_subarray(self):
        # given
        A = [1, 2, 3, 4, 5]
        expected_result = 15

        # when
        result, elapsed_time, memory_used = count_time_and_memory(search_max_subarray, A)

        # then
        self.assertEqual(result, expected_result)
        self.assertLess(elapsed_time, 2)
        self.assertLess(memory_used, 266144)

    def test2_should_check_success_search_max_subarray(self):
        # given
        A = [-1, -2, -3, -4, -5]
        expected_result = -1

        # when
        result, elapsed_time, memory_used = count_time_and_memory(search_max_subarray, A)

        # then
        self.assertEqual(result, expected_result)
        self.assertLess(elapsed_time, 2)
        self.assertLess(memory_used, 266144)

    def test3_should_check_success_search_max_subarray(self):
        # given
        A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected_result = 6

        # when
        result, elapsed_time, memory_used = count_time_and_memory(search_max_subarray, A)

        # then
        self.assertEqual(result, expected_result)
        self.assertLess(elapsed_time, 2)
        self.assertLess(memory_used, 266144)