import unittest
from lab5.utils import count_time_and_memory
from lab5.task1.src.heap_or_not import check_array


class AlgorithmsHeapTestCase(unittest.TestCase):

    def test1_should_check_success_check_array(self):
        # given
        n = 7
        A = [1, 2, 3, 4, 5, 6, 7]
        expected_result = 'YES'

        # when
        result, elapsed_time, memory_used = count_time_and_memory(check_array, n, A)

        # then
        self.assertEqual(result, expected_result)
        self.assertLess(elapsed_time, 2)
        self.assertLess(memory_used, 266144)

    def test2_should_check_unsuccess_check_array(self):
        # given
        n = 6
        A = [10, 15, 20, 30, 25, 5]
        expected_result = 'NO'

        # when
        result, elapsed_time, memory_used = count_time_and_memory(check_array, n, A)

        # then
        self.assertEqual(result, expected_result)
        self.assertLess(elapsed_time, 2)
        self.assertLess(memory_used, 266144)

    def test3_should_check_success_check_array(self):
        # given
        n = 5
        A = [2 * 10**9, 2 * 10**9 - 1, 2 * 10**9 - 2, 2 * 10**9 - 3, 2 * 10**9 - 4]
        expected_result = 'NO'

        # when
        result, elapsed_time, memory_used = count_time_and_memory(check_array, n, A)

        # then
        self.assertEqual(result, expected_result)
        self.assertLess(elapsed_time, 2)
        self.assertLess(memory_used, 266144)
