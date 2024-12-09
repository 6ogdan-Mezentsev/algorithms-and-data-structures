import unittest
from lab7.utils import count_time_and_memory
from lab7.task3.src.editorial_distance import edit_distance


class AlgorithmTestCase(unittest.TestCase):

    def test_should_check_success_primitive_calculate(self):
        # given
        s1 = 'editing'
        s2 = 'distance'
        expected_result = 5

        # when
        result, elapsed_time, memory_used = count_time_and_memory(edit_distance, s1, s2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLess(elapsed_time, 1)

