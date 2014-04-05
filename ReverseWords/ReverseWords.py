__author__ = 'ezequieldariogambaccini'


def solve_reverse(word_list):
    for i in xrange(len(word_list)/2):
        word_list[i], word_list[-i-1] = word_list[-i-1], word_list[i]

def Solve(in_file, out_file):
    with open(out_file, 'w') as out:
        with open(in_file, 'r') as in_data:
            N = int(in_data.readline())

            for x in xrange(N):
                l = in_data.readline().strip().split(" ")
                solve_reverse(l)

                res = "Case #%d: %s\n"%(x+1, " ".join(l))
                print(res)

                out.write(res)

if __name__ == "__main__":
    Solve("B-small-practice.in", "out_small.txt")
    print("Next set\n")
    Solve("B-large-practice.in", "out_large.txt")