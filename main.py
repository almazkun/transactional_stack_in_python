from tr_stack import TrStack
import timeit

if __name__ == "__main__":

    number = 10

    t_0 = "from tr_stack import TrStack; sol_0 = TrStack(); [sol_0.push(n) for n in range(1, 10**6)]"
    t_1 = "from tr_stack import TrStack; sol_0 = TrStack(); [sol_0.push(n) for n in range(1, 10**6)]"
    t_2 = "from tr_stack import TrStack; sol_0 = TrStack(); [sol_0.push(n) for n in range(1, 10**6)]"

    print(
        timeit.timeit(
            t_0,
            number=number,
        )
    )
    print(
        timeit.timeit(
            t_1,
            number=number,
        )
    )
    print(
        timeit.timeit(
            t_2,
            number=number,
        )
    )
