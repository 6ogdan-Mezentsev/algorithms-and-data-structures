import unittest
from lab6.utils import count_time_and_memory
from lab6.task1.src.set import set_commands


class AlgorithmsSetTestCase(unittest.TestCase):

    def test_should_check_success_set_commands(self):
        # given
        n = 8
        A = [('A', 2), ('A', 5), ('A', 3), ('?', 2), ('?', 4), ('A', 2), ('D', 2), ('?', 2)]
        expected_result = ['Y', 'N', 'N']

        # when
        result, elapsed_time, memory_used = count_time_and_memory(set_commands, A)

        # then
        self.assertEqual(result, expected_result)
        self.assertLess(elapsed_time, 2)
        self.assertLess(memory_used, 266144)

