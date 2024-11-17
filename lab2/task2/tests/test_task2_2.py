import unittest
from lab2.utils import count_time_and_memory
from lab2.task2.src.number_of_inversions import merge_sort_and_count


class AlgorithmsSortTestCase(unittest.TestCase):

    def test_test_should_check_success_of_counting_inversions(self):
        A = [5, 3, 2, 4, 1]  # не отсортированный массив, в котором 8 инверсий!!!
        n = len(A)  # кол-во элементов массива А
        expect_result = 8

        result, elapsed_time, memory_used = count_time_and_memory(merge_sort_and_count, A, n)

        print(f"\nВремя работы алгоритма_2: {elapsed_time:.6f} секунд")
        print(f"Использование памяти: {memory_used:.6f} Кб")

        self.assertEqual(result, expect_result)
        self.assertLess(elapsed_time, 2)
        self.assertLess(memory_used, 266144)
