from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, input().split())
    group_a = defaultdict(lambda: str(-1))

    for i in range(1, n + 1):
        word = input()
        if word in group_a:
            group_a[word] = group_a[word] + ' ' + str(i)
        else:
            group_a[word] = str(i)

    for _ in range(m):
        print(group_a[input()])
