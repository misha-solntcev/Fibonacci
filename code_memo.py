Dict = {0: 0, 1: 1}


def fib(n):
    if n not in Dict:
        Dict[n] = fib(n-2) + fib(n-1)
    return Dict[n]


if __name__ == "__main__":
    print(fib(10))
    print(Dict.values())
