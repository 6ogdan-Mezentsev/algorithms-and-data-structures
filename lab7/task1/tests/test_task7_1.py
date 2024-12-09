import unittest
from lab7.utils import count_time_and_memory
from lab7.task1.src.coin_exchange import min_coins


class AlgorithmTestCase(unittest.TestCase):

    def test_should_check_success_min_coins(self):
        # given
        money = 100
        coins = [1, 5, 10, 25, 50]
        expected_result = '2'

        # when
        result, elapsed_time, memory_used = count_time_and_memory(min_coins, money, coins)

        # then
        self.assertEqual(result, expected_result)
        self.assertLess(elapsed_time, 1)

