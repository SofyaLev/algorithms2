import unittest
from utils import memory_data, time_data
from lab4.task7.src.longest_common_substring import main, longest_common_substring


class TestLongestCommonSubstring(unittest.TestCase):

    def test_should_check_example1_data(self):
        # given
        data = ['cool', 'toolbox']
        expected_res = [1, 1, 3]

        # when
        res = longest_common_substring(data)

        # then
        self.assertEqual(res, expected_res)

    def test_should_check_example2_data(self):
        # given
        data = ['aaa', 'bb']
        expected_res = [0, 0, 0]

        # when
        res = longest_common_substring(data)

        # then
        self.assertEqual(res, expected_res)

    def test_should_check_example3_data(self):
        # given
        data = ['aabaa', 'babbaab']
        expected_res = [2, 3, 3]

        # when
        res = longest_common_substring(data)

        # then
        self.assertEqual(res, expected_res)

    def test_should_check_empty_data(self):
        # given
        data = ['', '']
        expected_res = [0, 0, 0]

        # when
        res = longest_common_substring(data)

        # then
        self.assertEqual(res, expected_res)

    def test_should_check_full_match_data(self):
        # given
        data = ['abc', 'abc']
        expected_res = [0, 0, 3]

        # when
        res = longest_common_substring(data)

        # then
        self.assertEqual(res, expected_res)

    def test_should_check_no_matches_data(self):
        # given
        data = ['aaa', 'bbb']
        expected_res = [0, 0, 0]

        # when
        res = longest_common_substring(data)

        # then
        self.assertEqual(res, expected_res)

    def test_should_check_big_data(self):
        # given
        data = ['a' * 10**4, 'a' * 10**4]
        expected_res = [0, 0, 10000]

        # when
        res = longest_common_substring(data)

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
