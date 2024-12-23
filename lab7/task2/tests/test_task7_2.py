import unittest
from lab7.utils import count_time_and_memory
from lab7.task2.src.primitive_calculator import primitive_calculator


class AlgorithmTestCase(unittest.TestCase):

    def test_should_check_success_primitive_calculate(self):
        # given
        n = 96234
        expected_result = (14, [1, 3, 9, 10, 11, 33, 99, 297, 891, 2673, 8019, 16038, 16039, 48117, 96234])

        # when
        result, elapsed_time, memory_used = count_time_and_memory(primitive_calculator, n)

        # then
        self.assertEqual(result, expected_result)
        self.assertLess(elapsed_time, 1)

