import pytz
import unittest
from datetime import datetime


class test_without_timezone(unittest.TestCase):
    def test_without_timezone(self):
        beginning_of_time = datetime(1970, 1, 1, 0, 0)

        with open("time.txt", "w+") as f:
            f.write(str(beginning_of_time))

        self.assertEqual(beginning_of_time.timestamp(), 0.0)

    def test_with_timezone(self):
        actual_beginning_of_time = datetime(
            1970, 1, 1, 0, 0, tzinfo=pytz.timezone("UTC")
        )
        breakpoint()
        self.assertEqual(actual_beginning_of_time.timestamp(), 0.0)


if __name__ == "__main__":
    unittest.main()
