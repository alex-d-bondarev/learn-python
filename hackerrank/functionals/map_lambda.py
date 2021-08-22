# Lambdas violate PEP 8: E731 do not assign a lambda expression, use a def


def fibonacci_expected(n):
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


def main_expected():
    print(list(map(cube, map(fibonacci_expected, range(int(input()))))))


def cube(n):
    return pow(n, 3)


def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[0:n]


# Predefined in hackerrank
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
