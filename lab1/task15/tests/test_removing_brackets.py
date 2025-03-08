import unittest
from utils import memory_data, time_data
from lab1.task15.src.removing_brackets import main, removing_brackets


class TestRemovingBrackets(unittest.TestCase):

    def test_should_check_example_data(self):
        # given
        data = '([)]'
        expected_res = '[]'

        # when
        res = removing_brackets(data)

        # then
        self.assertEqual(res, expected_res)

    def test_should_check_incorrect_data(self):
        # given
        data = ')('
        expected_res = ''

        # when
        res = removing_brackets(data)

        # then
        self.assertEqual(res, expected_res)

    def test_should_check_empty_data(self):
        # given
        data = ''
        expected_res = ''

        # when
        res = removing_brackets(data)

        # then
        self.assertEqual(res, expected_res)

    def test_should_check_time_data(self):
        # given
        expected_time = 2

        # when
        time = time_data(main)

        # then
        self.assertLess(time, expected_time)

    def test_should_check_memory_data(self):
        # given
        expected_memory = 256

        # when
        current, peak = memory_data(main)

        # then
        self.assertLess(current, expected_memory)
        self.assertLess(peak, expected_memory)


if __name__ == "__main__":
    unittest.main()
