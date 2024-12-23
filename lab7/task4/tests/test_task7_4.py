import unittest
from lab7.utils import count_time_and_memory
from lab7.task4.src.templates import check_template


class AlgorithmTestCase(unittest.TestCase):

    def test_should_check_success_check_template(self):
        # given
        pattern = 'k?t*n'
        A = 'kitten'
        ex_result = 'YES'

        # when
        result, elapsed_time, memory_used = count_time_and_memory(check_template, pattern, A)

        # then
        self.assertEqual(result, ex_result)
        self.assertLess(elapsed_time, 1)

