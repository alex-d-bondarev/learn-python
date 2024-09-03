from itertools import permutations

if __name__ == '__main__':
    S, k = input().split()
    perms = list(permutations(S, int(k)))
    perms.sort()

    for i in perms:
        print("".join(i))
