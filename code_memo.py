from typing import Dict
memo: Dict = {0: 0, 1: 1}  # базовые случаи


def fib(n):
    if n not in memo:
        memo[n] = fib(n-2) + fib(n-1)  # мемоизация
    return memo[n]


if __name__ == "__main__":
    print(fib(10))
    print(memo.values())
