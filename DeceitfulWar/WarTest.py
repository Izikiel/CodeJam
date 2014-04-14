__author__ = 'ezequieldariogambaccini'

import unittest

from DeceitfulWar import do_war
from DeceitfulWar import do_deceitful_war
from DeceitfulWar import SolveWar


class TestExamples(unittest.TestCase):
    def test_case1(self):
        naomi = [0.5]
        ken = [0.6]
        self.assertEqual(0, do_war(naomi, ken))

    def test_case2(self):
        naomi = [0.7, 0.2]
        ken = [0.8, 0.3]
        self.assertEqual(0, do_war(naomi, ken))

    def test_case3(self):
        naomi = [0.5, 0.1, 0.9]
        ken = [0.6, 0.4, 0.3]
        self.assertEqual(1, do_war(naomi, ken))

    def test_case4(self):
        naomi = [0.186, 0.389, 0.907, 0.832, 0.959, 0.557, 0.300, 0.992, 0.899]
        ken = [0.916, 0.728, 0.271, 0.520, 0.700, 0.521, 0.215, 0.341, 0.458]
        self.assertEqual(4, do_war(naomi, ken))


    def test_case_deceitful_1(self):
        naomi = [0.5]
        ken = [0.6]
        self.assertEqual(0, do_deceitful_war(naomi, ken))

    def test_case_deceitful_2(self):
        naomi = [0.7, 0.2]
        ken = [0.8, 0.3]
        self.assertEqual(1, do_deceitful_war(naomi, ken))

    def test_case_deceitful_3(self):
        naomi = [0.5, 0.1, 0.9]
        ken = [0.6, 0.4, 0.3]
        self.assertEqual(2, do_deceitful_war(naomi, ken))

    def test_case_deceitful_4(self):
        naomi = [0.186, 0.389, 0.907, 0.832, 0.959, 0.557, 0.300, 0.992, 0.899]
        ken = [0.916, 0.728, 0.271, 0.520, 0.700, 0.521, 0.215, 0.341, 0.458]
        self.assertEqual(8, do_deceitful_war(naomi, ken))

    def test_big(self):
        SolveWar("D-small-attempt1.in", "out_small1.txt")
        with open("out_small1.txt","r") as res:
            with open("out_small_ok1.txt", "r") as ok:
                for x in xrange(50):
                    self.assertEqual(res.readline(),ok.readline())


if __name__ == '__main__':
    unittest.main()
