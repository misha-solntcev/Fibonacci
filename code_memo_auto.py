from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:  # базовый случай
        return n
    return fib(n-2) + fib(n-1)  # рекурсивный случай


if __name__ == "__main__":
    print(fib(10))
