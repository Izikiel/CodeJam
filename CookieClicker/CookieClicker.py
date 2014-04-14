__author__ = 'ezequieldariogambaccini'

def min_cookie_time(farm_cost, cookie_increase, goal):
    cookies_per_second = 2.0
    total_time = 0.0

    current_performance = goal/cookies_per_second
    time_to_farm = farm_cost/cookies_per_second
    next_performance = time_to_farm + goal/(cookies_per_second+cookie_increase)

    if time_to_farm > current_performance:
        return current_performance

    while current_performance > next_performance:
        total_time += time_to_farm
        cookies_per_second += cookie_increase
        time_to_farm = farm_cost/cookies_per_second
        current_performance = goal/cookies_per_second
        next_performance = time_to_farm + goal/(cookies_per_second+cookie_increase)

    return total_time + current_performance


def SolveCookieClicker(in_file, out_file):
    with open(out_file, "w") as out_data:
        with open(in_file, "r") as in_data:
            N = int(in_data.readline())
            for i in xrange(N):
                r = "Case #%d: %.7f\n"%(i+1, min_cookie_time(*map(float, in_data.readline().split())))
                out_data.write(r)
                print(r)

if __name__ == "__main__":
    SolveCookieClicker("B-large-practice.in", "mine.txt")

