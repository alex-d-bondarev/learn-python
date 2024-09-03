def solution1(input_list):
    first = second = -101

    x: int
    for x in input_list:
        if x >= first:
            if x != first:
                second = first
            first = x
        elif x >= second:
            second = x

    print(second)


def solution2(input_list):
    print(sorted(set(input_list))[-2])


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    solution1(arr)
    solution2(arr)
