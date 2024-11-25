import unittest
from lab4.utils import count_time_and_memory
from lab4.task2.src.Queue import queue_commands


class AlgorithmsStackTestCase(unittest.TestCase):

    def test_should_check_success_queue_commands(self):
        # given
        commands = ['+10', '+20', '-', '+30', '-', '-']
        M = len(commands)
        expected_result = [10, 20, 30]

        # when
        result, elapsed_time, memory_used = count_time_and_memory(queue_commands, M, commands)

        # then
        self.assertEqual(result, expected_result)
        self.assertLess(elapsed_time, 2)
        self.assertLess(memory_used, 266144)
