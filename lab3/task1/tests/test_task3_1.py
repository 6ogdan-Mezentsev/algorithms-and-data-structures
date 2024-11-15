import unittest
import random
from lab3.utils import count_time_and_memory
from lab3.task1.src.QuickSort import Randomized_QuickSort, Partition3


class AlgorithmsSortTestCase(unittest.TestCase):

    def test_should_check_success_Randomized_Quick_Sorting(self):
        # given
        A = [random.randint(10**8, 10**9) for _ in range(10**4)]
        A_reverse_sort = sorted(A, reverse=True)
        n = len(A)

        # when
        result, elapsed_time, memory_used = count_time_and_memory(Randomized_QuickSort, A_reverse_sort, 0, len(A) - 1)
        print(f"\nВремя работы алгоритма_1: {elapsed_time:.6f} секунд")
        print(f"Использование памяти: {memory_used:.6f} Кб")

        # then
        self.assertEqual(result, sorted(A))  # проверка результата работы алгоритма
        self.assertLess(elapsed_time, 2)  # проверка времени выполнения
        self.assertLess(memory_used, 266144)  # проверка количества используемой памяти
