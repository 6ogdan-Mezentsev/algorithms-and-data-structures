import unittest
import random
from lab2.utils import count_time_and_memory
from lab2.task1.src.merge_sort import merge_sort


class AlgorithmsSortTestCase(unittest.TestCase):

    def test_should_check_success_merge_sorting(self):
        A = [random.randint(10**8, 10**9) for _ in range(20000)]
        A_reverse_sort = sorted(A, reverse=True)
        n = len(A)

        result, elapsed_time, memory_used = count_time_and_memory(merge_sort, A_reverse_sort, len(A))

        print(f"\nВремя работы алгоритма_1: {elapsed_time:.6f} секунд")
        print(f"Использование памяти: {memory_used:.6f} Кб")

        self.assertEqual(result, sorted(A))
