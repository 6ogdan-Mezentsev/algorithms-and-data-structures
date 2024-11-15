import unittest
from lab3.utils import count_time_and_memory
from lab3.task3.src.sort_by_scarecrow import can_sort_by_scarecrow


class AlgorithmsSortTestCase(unittest.TestCase):

    def test1_should_check_the_case_of_successful_sorting(self):
        # given
        n = 5
        k = 3
        sizes_of_matryoshkas = [1, 5, 3, 4, 1]

        # when
        result, elapsed_time, memory_used = count_time_and_memory(can_sort_by_scarecrow, n, k, sizes_of_matryoshkas)
        print(f"\nВремя работы алгоритма_3: {elapsed_time:.6f} секунд")
        print(f"Использование памяти: {memory_used:.6f} Кб")

        # then
        self.assertEqual(result, "ДА")

    def test2_should_check_the_case_of_impossible_sorting(self):
        # given
        n = 6
        k = 2
        sizes_of_matryoshkas = [3, 1, 4, 2, 6, 5]

        # when
        result, elapsed_time, memory_used = count_time_and_memory(can_sort_by_scarecrow, n, k, sizes_of_matryoshkas)
        print(f"\nВремя работы алгоритма_3: {elapsed_time:.6f} секунд")
        print(f"Использование памяти: {memory_used:.6f} Кб")

        # then
        self.assertEqual(result, "НЕТ")