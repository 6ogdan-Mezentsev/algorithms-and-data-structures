import unittest
from lab6.utils import count_time_and_memory
from lab6.task3.src.usa_elections import count_votes


class AlgorithmTestCase(unittest.TestCase):

    def test_should_check_success_phone_book_commands(self):
        # given
        A = ['ivanov 100', 'ivanov 500', 'ivanov 300', 'petr 70', 'tourist 1', 'tourist 2']
        expected_result = {'ivanov': 900, 'petr': 70, 'tourist': 3}

        # when
        result, elapsed_time, memory_used = count_time_and_memory(count_votes, A)

        # then
        self.assertEqual(result, expected_result)
        self.assertLess(elapsed_time, 2)
        self.assertLess(memory_used, 65536)

