import unittest
from lab6.utils import count_time_and_memory
from lab6.task5.src.hash_table import hash_table


class AlgorithmTestCase(unittest.TestCase):

    def test_should_check_success_fibonacci(self):
        # given
        N = 10
        X = 1
        A = 1
        B = 1
        AC = 0
        BC = 0
        AD = 1
        BD = 1

        expected_result = (108505111, 11, 11)

        # when
        result, elapsed_time, memory_used = count_time_and_memory(hash_table, N, X, A, B, AC, BC, AD, BD)

        # then
        self.assertEqual(result, expected_result)
        self.assertLess(elapsed_time, 5)
        self.assertLess(memory_used, 266144)

