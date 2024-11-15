import unittest
import random
from lab3.utils import count_time_and_memory
from lab3.task2.src.Anti_QuickSort import genearte_array


class AlgorithmsSortTestCase(unittest.TestCase):

    def test_should_check_success_generate_array(self):
        # given
        n = random.randint(900000, 10**6)

        # when
        result, elapsed_time, memory_used = count_time_and_memory(genearte_array, n)
        print(f"\nВремя работы алгоритма_2: {elapsed_time:.6f} секунд")
        print(f"Использование памяти: {memory_used:.6f} Кб")

        # then
        self.assertEqual(result, list(range(n, 0, -1)))