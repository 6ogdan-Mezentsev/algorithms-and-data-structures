import unittest
from lab6.utils import count_time_and_memory
from lab6.task2.src.phone_book import phone_book_commands


class AlgorithmTestCase(unittest.TestCase):

    def test_should_check_success_phone_book_commands(self):
        # given
        n = 10
        A = ['add 1234567 Alice', 'add 7654321 Bob', 'find 1234567', 'find 7654321', 'find 2345678', 'add 1234567 Charlie', 'find 1234567', 'del 1234567', 'find 1234567', 'find 7654321']
        expected_result = ['Alice', 'Bob', 'not found', 'Charlie', 'not found', 'Bob']

        # when
        result, elapsed_time, memory_used = count_time_and_memory(phone_book_commands, A)

        # then
        self.assertEqual(result, expected_result)
        self.assertLess(elapsed_time, 6)
        self.assertLess(memory_used, 266144)

