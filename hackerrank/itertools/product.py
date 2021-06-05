from itertools import product

if __name__ == '__main__':
    A = map(int, input().split())
    B = map(int, input().split())

    print(*product(A, B))