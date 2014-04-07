__author__ = 'ezequieldariogambaccini'


class Pattern(object):
    def __init__(self, s):
        self.pattern = self.parse(s)

    def parse(self, s):
        left_p = "("
        right_p = ")"

        pattern = []

        while True:
            if s.find(left_p) == -1:
                if len(s) > 0:
                    pattern.append(s)
                break
            l, sep, r = s.partition(left_p)

            if len(l) > 0:
                pattern.append(l)

            l, sep, r = r.partition(right_p)
            pattern.append(list(l))
            s = r

        return pattern

    def match(self, words):
        class res:
            val = 0

        def backtrack(pattern, words, s=""):
            if len(pattern) == 0:
                res.val += 1
                return

            p = pattern[0]
            if isinstance(p, list):
                for e in p:
                    if e in words:
                        backtrack(pattern[1:], words[e], s+e)
            else:
                check = p
                while len(check) > 0:
                    if check[0] in words:
                        words = words[check[0]]
                        check = check[1:]
                    else:
                        return

                backtrack(pattern[1:], words, s+p)

        backtrack(self.pattern, words)
        return res.val


_end = "_end_"

def make_trie(words):
    root = {}
    for w in words:
        actual = root
        for l in w:
            actual = actual.setdefault(l, {})
        actual = actual.setdefault(_end, _end)
    return root


def SolveAlienLang(in_file, out_file):
    with open(out_file, "w") as out_data:
        with open(in_file, "r") as in_data:
            w_len, n_words, N = map(int, in_data.readline().split())
            words = set()

            for _ in xrange(n_words):
                words.add(in_data.readline().strip())

            words = make_trie(words)

            for x in xrange(N):
                pattern_s = in_data.readline().strip()

                pattern = Pattern(pattern_s)

                r = "Case #%d: %d\n"%(x+1, pattern.match(words))

                out_data.write(r)
                print(r)

if __name__ == "__main__":
    SolveAlienLang("A-small-practice.in", "out_small.txt")
    print("\nNext set\n")
    SolveAlienLang("A-large-practice.in", "out_large.txt")