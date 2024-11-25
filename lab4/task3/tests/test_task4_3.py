import unittest
from lab4.utils import count_time_and_memory
from lab4.task3.src.bracket_sequence_v1 import check_correct_pairs


class AlgorithmsStackTestCase(unittest.TestCase):

    def test1_should_check_success_check_correct_pairs(self):
        # given
        sequence = '(())'
        expected_result = 'YES'

        # when
        result, elapsed_time, memory_used = count_time_and_memory(check_correct_pairs, sequence)
        print(f"\nВремя работы алгоритма_3: {elapsed_time:.6f} секунд")
        print(f"Использование памяти: {memory_used:.6f} Кб")

        # then
        self.assertEqual(result, expected_result)
        self.assertLess(elapsed_time, 2)
        self.assertLess(memory_used, 266144)

    def test2_should_check_UNsuccess_check_correct_pairs(self):
        # given
        sequence = '([)}]'
        expected_result = 'NO'

        # when
        result, elapsed_time, memory_used = count_time_and_memory(check_correct_pairs, sequence)

        # then
        self.assertEqual(result, expected_result)
        self.assertLess(elapsed_time, 2)
        self.assertLess(memory_used, 266144)
