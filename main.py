from tr_stack import TrStack
import timeit
from time import time
import concurrent.futures

import asyncio

if __name__ == "__main__":

    number = 1
    repeat = 5
    N = 10**7

    push = f"[sol_0.push(n) for n in range(1, {N})]"
    pull = f"[sol_0.pop() for _ in range({N})]"
    case_list_deque = [
        f"from tr_stack import TrStack; sol_0 = TrStack(); {push}; {pull}"
    ] * repeat

    case_list_list = [
        f"from tr_stack import TrStack; sol_0 = TrStack(list); {push}; {pull}"
    ] * repeat

    def print_result(case):
        print(
            f"for {N} push and pops: ",
            timeit.timeit(
                case,
                number=number,
            ),
        )

    print("With deque:")
    for case in case_list_deque:
        print_result(case)
    print("With list:")
    for case in case_list_list:
        print_result(case)
