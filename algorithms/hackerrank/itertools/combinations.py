from itertools import combinations

if __name__ == '__main__':
    S, k = input().split()

    for i in range(1, int(k) + 1):
        for c in list(combinations(sorted(S), i)):
            print("".join(c))
