__author__ = 'ezequieldariogambaccini'

primes_until_25 = [2, 3, 5, 7, 11, 13, 17, 19, 23]

def one_click_victory(rows, columns, mines):
    impossible = "Impossible"
    minimal_solutions = [1,4,6,8,9]
    total_cells = rows*columns
    free_spots = total_cells - mines
    if free_spots > max(minimal_solutions):
        return gen_solution(rows, columns, mines)
    if free_spots in minimal_solutions:
        return gen_solution(rows, columns, mines)
    if rows == 1 or columns == 1:
        return gen_solution(rows, columns, mines)
    return impossible



def gen_solution(rows, columns, mines):
    mine = "*"
    free = "."
    click = "c"
    free_spots = rows*columns - mines
    board = [[mine]*columns for _ in xrange(rows)]
    sq, i = is_square(free_spots)
    if rows == 1:
        for f in xrange(free_spots):
            board[0][f] = free
    elif columns == 1:
        for f in xrange(free_spots):
            board[f][0] = free
    elif sq:
        if i <= rows and i <= columns:
            for y in xrange(i):
                for x in xrange(i):
                    board[y][x] = free
            board[0][0] = click
    else:
        if free_spots%rows == 0:
            for y in xrange(rows):
                for x in xrange(free_spots/rows):
                    board[y][x] = free
        elif free_spots%columns == 0:
            for y in xrange(free_spots/columns):
                for x in xrange(columns):
                    board[y][x] = free

    board[0][0] = click

    return parse_board(board)

def parse_board(board):
    b = []
    for r in board:
        b.append("".join(r))
    return "\n".join(b)




def is_square(n):
    for i in xrange(1, 6):
        if n == i*i:
            return True, i
    return False, -1

def SolveMineSweeper(in_file, out_file):
    with open(out_file, "w") as out_data:
        with open(in_file, "r") as in_data:
            T = int(in_data.readline())
            for x in xrange(T):
                rows, columns, mines = map(int, in_data.readline().split())
                r = "Case #%d:\n%s\n"%(x+1, one_click_victory(rows, columns, mines))
                out_data.write(r)
                print(r)

if __name__ == "__main__":
    SolveMineSweeper("C-small-attempt0.in", "out_small0.txt")