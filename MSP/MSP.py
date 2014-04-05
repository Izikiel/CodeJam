__author__ = 'ezequieldariogambaccini'

def do_msp(v1, v2):
    v1.sort()
    v2.sort(reverse=True)

    return reduce(lambda r,(x,y): r + x*y, zip(v1,v2), 0)


def SolveMsp(in_file, out_file):
    with open(out_file, "w") as out_data:
        with open(in_file, "r") as in_data:
            T = int(in_data.readline())
            for x in xrange(T):
                v_len = int(in_data.readline())
                v1 = map(lambda x: int(x), in_data.readline().split(" "))
                v2 = map(lambda x: int(x), in_data.readline().split(" "))

                r = "Case #%d: %d\n"%(x+1, do_msp(v1, v2))

                out_data.write(r)
                print(r)

if __name__ == "__main__":
    SolveMsp("A-small-practice.in", "out_small.txt")
    print("\nNext set\n")
    SolveMsp("A-large-practice.in", "out_large.txt")
