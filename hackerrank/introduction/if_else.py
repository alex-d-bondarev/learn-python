#!/bin/python3


def even(number):
    return number % 2 == 0


if __name__ == '__main__':
    n = int(input().strip())
    weird = "Weird"
    not_weird = "Not Weird"

    if not even(n) or 6 <= n <= 20:
        output = weird
    else:
        output = not_weird

    print(output)
