import unittest
from lab2.utils import count_time_and_memory
from lab2.task3.src.element_of_majority import element_of_majority


class AlgorithmsSortTestCase(unittest.TestCase):

    def test1_should_check_presence_of_majority_element(self):
        A = [1]*10000 + [2]*5000 + [3]*4000  # массив, где 1 явлется элементом большинства

        result, elapsed_time, memory_used = count_time_and_memory(element_of_majority, A)

        print(f"\nВремя работы алгоритма_3: {elapsed_time:.6f} секунд")
        print(f"Использование памяти: {memory_used:.6f} Кб")

        self.assertEqual(result, 1)
        self.assertLess(elapsed_time, 2)
        self.assertLess(memory_used, 266144)

    def test2_should_check_missing_of_majority_element(self):
        A = [1]*5000 + [2]*5000 + [3]*5000  # массив, где нет элемента, который встречается более половины раз

        result, elapsed_time, memory_used = count_time_and_memory(element_of_majority, A)

        print(f"\nВремя работы алгоритма_3: {elapsed_time:.6f} секунд")
        print(f"Использование памяти: {memory_used:.6f} Кб")

        self.assertEqual(result, 0)
        self.assertLess(elapsed_time, 2)
        self.assertLess(memory_used, 266144)
