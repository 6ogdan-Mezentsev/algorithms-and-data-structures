import unittest
from lab5.utils import count_time_and_memory
from lab5.task2.src.height_of_tree import hight_of_tree


class AlgorithmsHeapTestCase(unittest.TestCase):

    def test_should_check_success_height_of_tree(self):
        # given
        n = 5
        parents = [-1, 0, 4, 0, 3]
        expected_result = '4'

        # when
        result, elapsed_time, memory_used = count_time_and_memory(hight_of_tree, n, parents)

        # then
        self.assertEqual(result, expected_result)
        self.assertLess(elapsed_time, 3)
        self.assertLess(memory_used, 266144)

