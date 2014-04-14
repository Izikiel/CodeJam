__author__ = 'ezequieldariogambaccini'

import unittest

from CookieClicker import min_cookie_time


class TestExamples(unittest.TestCase):
    def test_case1(self):
        t = min_cookie_time(30.0, 1.0, 2.0)
        self.assertEqual(1.0, t)

    def test_case2(self):
        t = min_cookie_time(30.0, 2.0, 100.0)
        self.assertEqual("39.1666667", "%.7f"%t)

    def test_case3(self):
        t = min_cookie_time(30.50000, 3.14159, 1999.19990)
        self.assertEqual('63.9680013', "%.7f"%t)

    def test_case4(self):
        t = min_cookie_time(500.0, 4.0, 2000.0)
        self.assertEqual("526.1904762", "%.7f"%t)

if __name__ == '__main__':
    unittest.main()
