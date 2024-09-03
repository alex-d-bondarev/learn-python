def initial_solution():
    stamps = set()
    first_set_size = int(input())
    for i in range(first_set_size):
        stamps.add(input().strip())
    print(len(stamps))


def one_liner_based_on_discussions():
    print(len({input() for _ in range(int(input()))}))


if __name__ == '__main__':
    # initial_solution()
    one_liner_based_on_discussions()
