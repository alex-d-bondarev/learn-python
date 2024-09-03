from itertools import combinations_with_replacement

if __name__ == '__main__':
    S, k = input().split()
    combs = list(combinations_with_replacement(sorted(S), int(k)))

    for i in combs:
        print("".join(i))
