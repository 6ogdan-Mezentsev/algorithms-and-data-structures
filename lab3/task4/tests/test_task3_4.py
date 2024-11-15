import unittest
from lab3.utils import count_time_and_memory
from lab3.task4.src.the_Hirsch_index import hirsch_index_search


class AlgorithmsSortTestCase(unittest.TestCase):

    def test1_should_check_the_search_for_Hirsch_index(self):
        # given
        citations = [3, 0, 6, 1, 5]

        # when
        result, elapsed_time, memory_used = count_time_and_memory(hirsch_index_search, citations)
        print(f"\nВремя работы алгоритма_4: {elapsed_time:.6f} секунд")
        print(f"Использование памяти: {memory_used:.6f} Кб")

        # then
        self.assertEqual(result, 3)

    def test2_should_check_the_search_for_Hirsch_index(self):
        # given
        citations = [10, 8, 5, 4, 3]

        # when
        result, elapsed_time, memory_used = count_time_and_memory(hirsch_index_search, citations)
        print(f"\nВремя работы алгоритма_4: {elapsed_time:.6f} секунд")
        print(f"Использование памяти: {memory_used:.6f} Кб")

        # then
        self.assertEqual(result, 4)  # проверка результата работы алгоритма
        self.assertLess(elapsed_time, 2)  # проверка времени выполнения
        self.assertLess(memory_used, 266144)  # проверка количества используемой памяти
