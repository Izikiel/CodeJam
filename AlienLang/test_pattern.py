from unittest import TestCase

from AlienLang import make_trie, Pattern


__author__ = 'ezequieldariogambaccini'


class TestPattern(TestCase):
    res = [2,1,3,0]
    words = make_trie(["abc","bca","dac","dbc","cba"])
    pattern_list = ["(ab)(bc)(ca)","abc","(abc)(abc)(abc)","(zyx)bc"]
    parsed_patterns = [
        [
            ["a","b"], ["b","c"], ["c","a"],
        ] ,
        [
            "abc"
        ],
        [
            ["a","b","c"],["a","b","c"],["a","b","c"],
        ],
        [
            ["z", "y", "x"], "bc"
        ],
    ]

    def testParse(self):
        for i in xrange(len(TestPattern.pattern_list)):
            p = Pattern(TestPattern.pattern_list[i])
            self.assertEqual(self.parsed_patterns[i], p.pattern, "Bad Parse")


    def testMatch(self):
        for i in xrange(len(TestPattern.pattern_list)):
            p = Pattern(TestPattern.pattern_list[i])
            self.assertEqual(TestPattern.res[i], p.match(TestPattern.words), "Bad Match")
