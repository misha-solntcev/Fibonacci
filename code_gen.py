from typing import Generator


def fib(n) -> Generator[int, None, None]:
    yield 0  # специальный случай
    if n > 0:
        yield 1  # специальный случай
    last = 0  # начальное значение fib(0)
    next = 1  # начальное значение fib(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next  # главный этап генерации


if __name__ == "__main__":
    F = []
    for i in fib(15):
        F.append(i)
    print(F)
