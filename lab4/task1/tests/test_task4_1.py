import unittest
from lab4.utils import count_time_and_memory
from lab4.task1.src.stack_1 import stack_commands


class AlgorithmsStackTestCase(unittest.TestCase):

    def test_should_check_success_stack_commands(self):
        # given
        commands = ['+1', '+5', '-', '+10', '-', '+2', '-', '+1234', '-', '+23', '-']
        M = len(commands)
        expected_result = [5, 10, 2, 1234, 23]

        # when
        result, elapsed_time, memory_used = count_time_and_memory(stack_commands, M, commands)

        # then
        self.assertEqual(result, expected_result)
        self.assertLess(elapsed_time, 2)
        self.assertLess(memory_used, 266144)
