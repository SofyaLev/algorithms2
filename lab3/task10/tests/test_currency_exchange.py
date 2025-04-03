import unittest
from utils import memory_data, time_data
from lab3.task10.src.currency_exchange import main, currency_exchange


class TestCurrencyExchange(unittest.TestCase):

    def test_should_check_example1_data(self):
        # given
        data = [[6, 7], [1, 2, 10], [2, 3, 5], [1, 3, 100], [3, 5, 7], [5, 4, 10], [4, 3, -18], [6, 1, -1], [1]]
        expected_res = [0, 10, '-', '-', '-', '*']

        # when
        res = currency_exchange(data)

        # then
        self.assertEqual(res, expected_res)

    def test_should_check_example2_data(self):
        # given
        data = [[5, 4], [1, 2, 1], [4, 1, 2], [2, 3, 2], [3, 1, -5], [4]]
        expected_res = ['-', '-', '-', 0, '*']

        # when
        res = currency_exchange(data)

        # then
        self.assertEqual(res, expected_res)

    def test_should_check_time_data(self):
        # given
        expected_time = 10

        # when
        time = time_data(main)

        # then
        self.assertLess(time, expected_time)

    def test_should_check_memory_data(self):
        # given
        expected_memory = 512

        # when
        current, peak = memory_data(main)

        # then
        self.assertLess(current, expected_memory)
        self.assertLess(peak, expected_memory)


if __name__ == "__main__":
    unittest.main()
