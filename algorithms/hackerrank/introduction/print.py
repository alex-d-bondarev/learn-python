import sys

if __name__ == '__main__':
    n = int(input()) + 1

    values = set()
    for i in range(1, n):
        values.add(i)

    print(*values, sep='', end='\n', file=sys.stdout)
