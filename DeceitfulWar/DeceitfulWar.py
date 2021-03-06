__author__ = 'ezequieldariogambaccini'

"""
ChosenNaomi > ChosenKen if, and only if, ToldNaomi > ChosenKen, and
ToldNaomi is not equal to the mass of any of Ken's blocks, because he knows that isn't possible.
"""

def do_war(naomi, ken): #tiene q ganar ken
    N = len(naomi)

    s_naomi = sorted(naomi)
    s_ken = sorted(ken)

    i = 0
    while len(s_ken) > 0:
        head = s_ken.pop(0)
        if head > s_naomi[0]: #ordenado, el primero es el mas chico
            i += 1
            s_naomi.pop(0)
        else:
            s_naomi.pop(-1)

    return N-i



def do_deceitful_war(naomi, ken):
    if max(naomi) < min(ken):
        return 0

    s_naomi = sorted(naomi)
    s_ken = sorted(ken)

    best_war = 0

    while len(s_naomi) > 0:
        head = s_naomi.pop(0)
        # metodo mas rapido (?)
        if head > s_ken[0]: #ordenado, el primero es el mas chico
            best_war += 1
            s_ken.pop(0)
        else:
            s_ken.pop(-1)
        # metodo mas declarativo :O
        # if any(map(lambda elem: head > elem, s_ken)):
        #     best_war += 1
        #     s_ken.remove(filter(lambda elem: head > elem, s_ken)[0])
        # else:
        #     s_ken.remove(max(s_ken))
        # s_naomi.remove(head)

    return best_war


def SolveWar(in_file, out_file):
    with open(out_file, "w") as out_data:
        with open(in_file, "r") as in_data:
            T = int(in_data.readline())
            for x in xrange(T):
                N = int(in_data.readline())
                naomi = map(float, in_data.readline().split())
                ken = map(float, in_data.readline().split())
                war = do_war(naomi, ken)
                d_war = do_deceitful_war(naomi, ken)
                r = "Case #%d: %d %d\n"%(x+1, d_war, war)

                print(r)
                out_data.write(r)

if __name__ == "__main__":
    # SolveWar("D-small-attempt0.in", "out_small0.txt")
    # SolveWar("D-small-attempt1.in", "out_small1.txt")
    SolveWar("D-large.in", "out_large.txt")