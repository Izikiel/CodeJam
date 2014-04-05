__author__ = 'ezequieldariogambaccini'

def solve_items(credit, number_of_items, item_prices):
    items = {}
    for i, v in enumerate(item_prices):
        if credit - v in items:
            return items[credit-v], i
        else:
            items[v] = i
    return None


def SolveCreditStore(file_name, out_file):
    with open(out_file,'w') as out:
        with open(file_name, 'r') as f_input:
            N = int(f_input.readline())
            for x in xrange(N):
                credit = int(f_input.readline())
                number_of_items = int(f_input.readline())
                item_prices = map(lambda x: int(x), f_input.readline().split(" "))

                res = solve_items(credit, number_of_items, item_prices)

                assert res is not None
                a, b = res
                out.write("Case #%d: %d %d\n"%(x+1, a+1, b+1))
                print("Case #%d: %d %d"%(x+1, a+1, b+1))


if __name__ == "__main__":
    SolveCreditStore("A-small-practice.in", "out_small.txt")
    print("\nNext set\n")
    SolveCreditStore("A-large-practice.in", "out_large.txt")