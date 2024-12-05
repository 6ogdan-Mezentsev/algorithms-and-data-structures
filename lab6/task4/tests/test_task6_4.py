import unittest
from lab6.utils import count_time_and_memory
from lab6.task4.src.fib_nums import fibonacci


class AlgorithmTestCase(unittest.TestCase):

    def test_should_check_success_fibonacci(self):
        # given
        n = 5
        A = [144, 233, 987, 1597, 987654321987654321987654321]
        expected_result = ['Yes', 'Yes', 'Yes', 'Yes', 'No']

        # when
        result, elapsed_time, memory_used = count_time_and_memory(fibonacci, A)

        # then
        self.assertEqual(result, expected_result)
        self.assertLess(elapsed_time, 2)
        self.assertLess(memory_used, 131072)

