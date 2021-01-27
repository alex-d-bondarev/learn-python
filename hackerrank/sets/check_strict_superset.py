def initial_solution():
    global all_are_supersets
    for _ in range(n):
        other_set = set(map(int, input().split()))
        all_are_supersets = all_are_supersets and a_set.issuperset(other_set)
    print(all_are_supersets)


def shorter_solution():
    print(all(a_set.issuperset(set(map(int, input().split()))) for _ in range(n)))


if __name__ == '__main__':
    a_set = set(map(int, input().split()))
    all_are_supersets = True
    n = int(input())

    # initial_solution()
    shorter_solution()
