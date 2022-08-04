from tr_stack import TrStack
import timeit

if __name__ == "__main__":

    number = 1

    print(
        timeit.timeit(
            "from tr_stack import TrStack; sol_0 = TrStack(); [sol_0.push(n) for n in range(1, 10**6)]",
            number=number,
        )
    )
