import unittest
import random
from lab2.utils import count_time_and_memory
from lab2.task4.src.binary_search import binary_search


class AlgorithmsSortTestCase(unittest.TestCase):

    def test_should_check_success_of_binary_search(self):
        # given
        lst = sorted(random.sample(range(1, 10000000), 10000))
        value = lst[3000]

        # when
        result, elapsed_time, memory_used = count_time_and_memory(binary_search, value, lst)

        # then
        self.assertEqual(result, binary_search(value, lst))
        self.assertLess(elapsed_time, 2)
        self.assertLess(memory_used, 266144)
