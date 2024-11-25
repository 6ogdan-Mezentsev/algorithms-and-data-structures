import unittest
from lab4.utils import count_time_and_memory
from lab4.task4.src.Queue_with_min import queue_commands_min


class AlgorithmsStackTestCase(unittest.TestCase):

    def test_should_check_success_queue_commands_min(self):
        # given
        commands = ['+3', '+2', '?', '-', '?', '+5', '+1', '?', '-', '?']
        M = len(commands)
        expected_result = [2, 2, 1, 1]

        # when
        result, elapsed_time, memory_used = count_time_and_memory(queue_commands_min, M, commands)

        # then
        self.assertEqual(result, expected_result)
        self.assertLess(elapsed_time, 2)
        self.assertLess(memory_used, 266144)

