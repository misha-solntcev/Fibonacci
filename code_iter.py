def fib(n):
    F = []
    last = 0  # начальное значение fib(0)
    next = 1  # начальное значение fib(1)
    F.append(last)
    F.append(next)
    for _ in range(1, n):
        last, next = next, last + next
        F.append(next)
    print(F)


if __name__ == "__main__":
    fib(10)
