import unittest
from lab3.utils import count_time_and_memory
from lab3.task6.src.nearest_points_to_the_beginning import distance_search


class AlgorithmsSortTestCase(unittest.TestCase):

    def test_should_check_success_of_distance_search(self):
        # given
        n = 3
        k = 1
        points = [(1000, 1000), (2000, 2000), (-3000, -3000)]
        expected_result = [(1000, 1000)]

        # when
        result, elapsed_time, memory_used = count_time_and_memory(distance_search, n, k, points)
        print(f"\nВремя работы алгоритма_6: {elapsed_time:.6f} секунд")
        print(f"Использование памяти: {memory_used:.6f} Кб")

        # then
        self.assertEqual(distance_search(3, 1, points), expected_result)  # проверка результата работы алгоритма
        self.assertLess(elapsed_time, 2)  # проверка времени выполнения
        self.assertLess(memory_used, 266144)  # проверка количества используемой памяти
