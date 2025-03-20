import unittest
from utils import memory_data, time_data
from lab2.task8.src.tree_height import main, tree_height


class TestTreeHeight(unittest.TestCase):

    def test_should_check_example_data(self):
        # given
        data = [[6], [-2, 0, 2], [8, 4, 3], [9, 0, 0], [3, 6, 5], [6, 0, 0], [0, 0, 0]]
        expected_res = 4

        # when
        res = tree_height(data)

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
