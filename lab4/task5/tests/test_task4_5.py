import unittest
from lab4.utils import count_time_and_memory
from lab4.task5.src.Postfix_entry import Postfix_calculate


class AlgorithmsStackTestCase(unittest.TestCase):

    def test_should_check_success_queue_commands_min(self):
        # given
        expression = '3 4 + 2 * 7 /'
        expected_result = 2

        # when
        result, elapsed_time, memory_used = count_time_and_memory(Postfix_calculate, expression)

        # then
        self.assertEqual(result, expected_result)
        self.assertLess(elapsed_time, 2)
        self.assertLess(memory_used, 266144)

