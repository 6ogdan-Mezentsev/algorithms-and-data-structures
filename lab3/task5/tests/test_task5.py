import unittest
from lab3.utils import count_time_and_memory
from lab3.task1.src.QuickSort import Randomized_QuickSort, Partition3
from lab3.task5.src.sort_int import sorting_integers


class AlgorithmsSortTestCase(unittest.TestCase):

    def test_should_check_success_sorting_integers(self):
        # given
        A = [i for i in range(1, 1001)]
        B = [i for i in range(1001, 2001)]

        # when
        result, elapsed_time, memory_used = count_time_and_memory(sorting_integers, A, B)
        print(f"\nВремя работы алгоритма_5: {elapsed_time:.6f} секунд")
        print(f"Использование памяти: {memory_used:.6f} Кб")

        # then
        self.assertEqual(result, 75099133529)
