__author__ = 'ezequieldariogambaccini'

import unittest

from MineSweeper import one_click_victory

class TestExamples(unittest.TestCase):
    impossible = "Impossible"
    def test_case1(self):
        r = one_click_victory(*[5,5,23])
        self.assertEqual(self.impossible, r)

    def test_case2(self):
        r = one_click_victory(*[3,1,1])
        self.assertIsNotNone(r)
        self.assertNotEqual(self.impossible, r)

    def test_case3(self):
        r = one_click_victory(*[2,2,1])
        self.assertEqual(self.impossible, r)

    def test_case4(self):
        r = one_click_victory(*[4,7,3])
        self.assertIsNotNone(r)
        self.assertNotEqual(self.impossible, r)

    def test_case5(self):
        r = one_click_victory(*[10,10,82])
        self.assertIsNotNone(r)
        self.assertNotEqual(self.impossible, r)

    def test_case6(self):
        r = one_click_victory(5,5,20)
        self.assertEqual(self.impossible, r)

    def test_case7(self):
        r = one_click_victory(4,5,18)
        self.assertEqual(self.impossible, r)


if __name__ == '__main__':
    unittest.main()
